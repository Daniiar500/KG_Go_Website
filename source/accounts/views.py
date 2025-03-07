from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.urls import reverse

from accounts.forms import UserChangeForm
from webapp.models import Player, Club


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        if kwargs['object'].pk == 1 and not self.request.user.is_superuser:
            raise PermissionDenied()
        else:
            context = super().get_context_data(**kwargs)
            coach = self.get_object()
            coach_clubs = []
            coach_students = []
            for club in coach.clubs.all():
                coach_clubs.append(club.pk)
            for player in Player.objects.all():
                for each_club in player.clubs.all():
                    if each_club.pk in coach_clubs:
                        coach_students.append(player.pk)
            data = Player.objects.filter(pk__in=coach_students)
            context['players'] = data
            club_names = []
            for e in coach.clubs.all():
                club_names.append(e.name)
            context['club_names'] = club_names
            return context


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            coach_club_id = form.cleaned_data['coach_club']
            if coach_club_id:
                coach = get_object_or_404(get_user_model(), pk=self.request.user.pk)
                for club in (Club.objects.filter(coaches__exact=coach.pk)):
                    club.coaches.remove(coach)
                for club in Club.objects.all():
                    if str(club.pk) in coach_club_id:
                        club.coaches.add(coach)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.get_object().pk})
