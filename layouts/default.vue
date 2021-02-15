<template lang="pug">
  div
    Navbar(:mainPage="true")
    .wrapper
      nuxt
    Footer
</template>

<script>
import Navbar from "~/components/nav/Navbar.vue";
import Footer from "~/components/Footer.vue";

export default {
  layout: "page",
  components: {
    Navbar,
    Footer,
  },

  // need to call BEFORE load
  // this still leaves a flash of light
  beforeMount() {
    // this also needs to be on ALL page loads
    // there doesn't seem to be a main root App.vue for Nuxt
    this.$store.commit("themestore/setThemeOnPageVisit");
  },
};
</script>

<style lang="scss">
@import "./styles/globals.scss";
@import "./styles/main.scss";

body {
  background-color: var(--nav-background-color);

  .wrapper {
    min-height: 95vh;
    background-color: var(--background-color);
  }
}
</style>
