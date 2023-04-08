<script lang="ts">
  import { onMount } from "svelte";
  let url = "";

  let message = "Loading...";
  function load() {
    fetch(url + "/api/helloworld/sampledocument")
      .then((response) => response.json())
      .then((data) => {
        message = data["message"];
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
    url = window.location.origin;
    if (import.meta.env.DEV) {
      url = "http://localhost:8080";
    }
  }

  onMount(async () => {
    load();
  });
</script>

<h1>Bootstrap</h1>
<p>Backend URL is : {url}</p>
<p>{message}</p>
