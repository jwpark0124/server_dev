from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from .serializers import SignupSerializer


# def logout(request):
#     messages.success(request, '로그아웃되었습니다.')
#     return logout_then_login(request)




class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

# @login_required
# def profile_edit(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "프로필을 수정/저장했습니다.")
#             return redirect("profile_edit")
#     else:
#         form = ProfileForm(instance=request.user)
#     return render(request, "accounts/profile_edit_form.html", {
#         "form": form,
#     })
    

# class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
#     success_url = reverse_lazy("password_change")
#     template_name = 'accounts/password_change_form.html'
#     form_class = PasswordChangeForm

#     def form_valid(self, form):
#         messages.success(self.request, "암호를 변경했습니다.")
#         return super().form_valid(form)

# password_change = PasswordChangeView.as_view()
