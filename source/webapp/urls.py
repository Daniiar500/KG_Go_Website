from django.urls import path

from .views import FileUpload, TournamentCheckView, IndexView, NewsListView, PlayerSearch, TournamentSearch, CalendarCreateView, \
    CalendarUpdateView, CalendarDeleteView, CompetitorSearch, ClubsListView, PlayerDetail, TournamentDetail, \
    NewsCreateView, NewsDetailView, NewsUpdateView, NewsDeleteView, DeletedNewsListView, restore_one_deleted_news, \
    hard_delete_one_news, UpdatePlayer, about_us_view, DeletePlayer, ClubUpdate, ParticipantCreate, \
    CalendarDetailView, ClubView, DeletedCalendarListView, restore_one_deleted_event, \
    hard_delete_one_event, RecommendationCreateView, send_feedback_to_admin, RecommendationUpdateView, \
    RecommendationDeleteView, StatusChange, DeletePlayerFromEvent, calendar_player_list, PartnerCreateView, \
    PartnersListView, PartnerDetailView, PartnerUpdateView, PartnerDeleteView, UpdateParticipant, ClubCreate, \
    TournamentModerationList, DeleteTournamentBeforeModeration, ModerationTournamentView, DeleteTournamentOnModeration, \
    PlayerDetailGames, PlayerDetailGorEvolution, CarouselCreateView, CarouselUpdateView, CarouselDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('player_search/', PlayerSearch.as_view(), name='player_search'),
    path('player_detail/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('update_player/<int:pk>/', UpdatePlayer.as_view(), name='update_player'),
    path('delete_player/<int:pk>/', DeletePlayer.as_view(), name='delete_player'),
    path('file_upload/', FileUpload.as_view(), name='file_upload'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/deleted_list/', DeletedNewsListView.as_view(), name='deleted_news_list'),
    path('news/restore/<int:pk>/', restore_one_deleted_news, name='news_restore_one_deleted'),
    path('news/hard_delete/<int:pk>/', hard_delete_one_news, name='news_hard_delete_one'),
    path('news_create/', NewsCreateView.as_view(), name='news_create'),
    path('news_detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news_update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('news_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('clubs/', ClubsListView.as_view(), name='clubs_list'),
    path('clubs/<int:pk>/', ClubView.as_view(), name='club_view'),
    path('club_create/', ClubCreate.as_view(), name='club_create'),
    path('club_update/<int:pk>/', ClubUpdate.as_view(), name='club_update'),
    path('event_create/', CalendarCreateView.as_view(), name='event_create'),
    path('event_update/<int:pk>/', CalendarUpdateView.as_view(), name='event_update'),
    path('event_delete/<int:pk>/', CalendarDeleteView.as_view(), name='event_delete'),
    path('event_view/<int:pk>/', CalendarDetailView.as_view(), name='event_view'),
    path('event_restore/<int:pk>/', restore_one_deleted_event, name='event_restore_one_deleted'),
    path('event_hard_delete/<int:pk>/', hard_delete_one_event, name='event_hard_delete_one'),
    path('deleted_events_list/', DeletedCalendarListView.as_view(), name='deleted_calendar_list'),
    path('tournament_search/', TournamentSearch.as_view(), name='tournament_search'),
    path('tournament_search/<int:pk>/', TournamentDetail.as_view(), name='tournament_detail'),
    path('competitors/<int:pk>/', CompetitorSearch.as_view(), name='competitor_search'),
    path('about/', about_us_view, name='about'),
    path('feedback_to_mail/', send_feedback_to_admin, name='feedback_to_admin'),
    path('file_check/<str:file_name>/', TournamentCheckView.as_view(), name='file_check'),
    path('file_check/<str:file_name>/delete/', DeleteTournamentBeforeModeration.as_view(), name='delete_tournament'),
    path('participiant_create/<int:pk>/', ParticipantCreate.as_view(), name='ParticipantCreate'),
    path('player_detail/<int:pk>/recommendation_add/', RecommendationCreateView.as_view(), name='recommendation_add'),
    path('recommendation/<int:pk>/update', RecommendationUpdateView.as_view(), name='recommendation_update'),
    path('recommendation_delete/<int:pk>/', RecommendationDeleteView.as_view(), name='recommendation_delete'),
    path('event_player/<int:pk>/', calendar_player_list, name='CalendarPlayerList'),
    path('status/<int:pk>/', StatusChange.as_view(), name='status_change'),
    path('deleteplayerfromevent/<int:pk>/', DeletePlayerFromEvent.as_view(), name='delete_player_from_event'),
    path('update_participant/<int:pk>/', UpdateParticipant.as_view(), name='update_participant'),
    path('partner_create/', PartnerCreateView.as_view(), name='partner_create'),
    path('partners/', PartnersListView.as_view(), name='partners_list'),
    path('partner_detail/<int:pk>/', PartnerDetailView.as_view(), name='partner_detail'),
    path('partner_update/<int:pk>/', PartnerUpdateView.as_view(), name='partner_update'),
    path('partner_delete/<int:pk>/', PartnerDeleteView.as_view(), name='partner_delete'),
    path('moderation_tournaments/', TournamentModerationList.as_view(), name='moderation_tournaments'),
    path('cancel_tournament/<int:pk>/', DeleteTournamentOnModeration.as_view(), name='delete_tournament_on_moderation'),
    path('moderation_tournaments/<int:pk>/', ModerationTournamentView.as_view(), name='tournament_moderation_detail'),
    path('player_detail/<int:pk>/games/', PlayerDetailGames.as_view(), name='player_detail_games'),
    path('player_detail/<int:pk>/evolution/', PlayerDetailGorEvolution.as_view(), name='player_gor_evolution'),
    path('carousel_create/', CarouselCreateView.as_view(), name='create_carousel'),
    path('carousel_update/<int:pk>/', CarouselUpdateView.as_view(), name='update_carousel'),
    path('carousel_delete/<int:pk>/', CarouselDeleteView.as_view(), name='delete_carousel')
]

handler400 = 'webapp.views.error_views.custom_handler400'
handler403 = 'webapp.views.error_views.custom_handler403'
handler404 = 'webapp.views.error_views.custom_handler404'
handler500 = 'webapp.views.error_views.custom_handler500'
