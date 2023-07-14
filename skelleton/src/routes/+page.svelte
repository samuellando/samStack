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
	var backend = true;

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
        try {
            await apiClient.post('example/example', { message: 'Hello, World! ... From the backend' });
        } catch (error) {
            try {
                await apiClient.put('example/example', { message: 'Hello, World! ... From the backend' });
            } catch (error) {
                console.log(error);
                backend = false;
            }
        }
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
    {#if backend}
        {#await apiClient.get("example/example")}
            <p>Waiting for backend...</p>
        {:then response}
            <p>{response["message"]}</p>
        {:catch error}
            <p>Backend error: {error.message}</p>
        {/await}
    {/if}
{/if}

