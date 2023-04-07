import { create } from 'create-svelte';

var p = process.argv[2];

await create(p, {
  name: p,
  template: 'skeleton', // or 'skeleton' or 'skeletonlib'
  types: 'typescript', // or 'typescript' or null;
  prettier: true,
  eslint: true,
  playwright: true,
  vitest: true
});
