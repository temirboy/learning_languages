class LanguageMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        # print("111111")

        response = self._get_response(request)
        var = request.session.get('lang', 'asd')
        # print(var)
        # print("222222")
        # request.session['username1'] = 'qwe'
        # request.session.modified = True
        # var = request.session.get('username1', 'qwe')
        # print(var)
        # del request.session['username1']
        return response

    #def process_exception(self, request, exception):
        #print(f'exset is - {exception}')
