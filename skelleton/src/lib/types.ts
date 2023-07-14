export interface apiKey {
  apiKey: string;
}

import type { Auth0Client, User } from '@auth0/auth0-spa-js';

export interface authDef {
  authClient: Auth0Client | undefined,
  isAuthenticated: boolean,
  userProfile: User | undefined,
  accessToken: string | undefined
}
