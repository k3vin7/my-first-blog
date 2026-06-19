from rest_framework.authentication import TokenAuthentication


class JWTPrefixTokenAuthentication(TokenAuthentication):
    keyword = 'JWT'
