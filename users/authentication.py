from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.exceptions import TokenError, AuthenticationFailed

class BlacklistCheckJWTAuthentication(JWTAuthentication):
    """
    Extends default JWT auth to reject access tokens that have been blacklisted.
    By default, SimpleJWT only blacklists refresh tokens — this covers access tokens too.
    """

    def get_validated_token(self, raw_token):
        validated_token = super().get_validated_token(raw_token)

        jti = validated_token.get('jti')

        if jti:
            try:
                outstanding = OutstandingToken.objects.get(jti=jti)
                if BlacklistedToken.objects.filter(token=outstanding).exists():
                    raise AuthenticationFailed('Token has been blacklisted (user logged out).')
            except OutstandingToken.DoesNotExist:
                pass  # Token not tracked, allow it through

        return validated_token