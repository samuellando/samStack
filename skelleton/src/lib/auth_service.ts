import { createAuth0Client } from "@auth0/auth0-spa-js";
import config from "$src/auth_config";

async function createClient(redirect: string) {
  let auth0Client = await createAuth0Client({
    domain: config.domain,
    clientId: config.clientId,
    authorizationParams: {
      redirect_uri: redirect,
      audience: config.audience,
      scope: "timelogger:read"
    },
    useRefreshTokens: true,
    cacheLocation: 'localstorage'
  });

  return auth0Client;
}

export default createClient;
