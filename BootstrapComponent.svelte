<script lang="ts">
  let url2 = window.location.origin;
  let url = "";
  if (import.meta.env.DEV) {
    url2 = "http://localhost:8080";
  }
  import { onMount } from "svelte";

  let message = "Loading...";
  function load() {
    fetch(url + "/api")
      .then((response) => response.json())
      .then((data) => {
        message = data["message"];
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
    url = url2;
  }

  onMount(async () => {
    load();
  });
</script>

<p>Backend URL is : {url}</p>
<p>{message}</p>
