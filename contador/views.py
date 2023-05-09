from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class CountAPIView(View):
    template_name = 'count.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "count", {"type": "count_message", "text": "add"}
        )
        return JsonResponse({'success': True})