<script lang="ts">
	import { onMount, afterUpdate } from 'svelte';
	import Auth from '$lib/components/Auth.svelte';
	import { auth } from '$lib/Auth';
	import type { authDef } from '$lib/types';
    import { BaseClient } from '$lib/BaseClient';

	var authDef: authDef = {
		authClient: undefined,
		isAuthenticated: false,
		userProfile: undefined,
		accessToken: undefined
	};

	var loading = true;

    let apiUrl: string;
    let apiClient: BaseClient;

	onMount(async () => {
		authDef = await auth();
		apiUrl = window.location.origin;
		if (import.meta.env.DEV) {
			apiUrl = 'http://localhost:8080';
		}
		//authDef = await auth();
        apiClient = new BaseClient(apiUrl);
        await apiClient.post('example/example', { message: 'Hello, World! ... From the backend' });
		loading = false;
	});

	afterUpdate(() => {
		if (authDef.isAuthenticated) {
			window.location.pathname = '/logged-in';
		}
	});
</script>

{#if loading}
    <p>Loading...</p>
{:else}
    <Auth {authDef} />

    <h1>Wellcome to the SamStack</h1>
    <p>{apiClient.get("example/example")["message"]}</p>
{/if}

