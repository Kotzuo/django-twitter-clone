from rest_framework import filters


class FollowingOnlyFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('following') == 'true':
            return queryset.filter(
                owner__in=request.user.following.all()
            )

        return queryset
