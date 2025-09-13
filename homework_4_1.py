class BaseView:
    def render(self):
        print("Template render")

class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")

class AuthRequiredMixin:
    def __init__(self, authed=True):
        self.authed = authed

    def render(self):
        if self.authed:
            print("Log OK")
            super().render()
        else:
            print("Access denied")

class AdminPageView(LoggingMixin,AuthRequiredMixin, BaseView):
    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")

print("---- Авторизованный: ----")
admin_ok = AdminPageView(authed=True)
admin_ok.render()

print("\n---- Неавторизованный: ----")
admin_fail =AdminPageView(authed=False)
admin_fail.render()



