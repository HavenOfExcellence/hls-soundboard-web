<template lang="pug">
  .soundboard
    .sounds
      SoundButton(v-for="sound in this.sounds" :fileName="sound" v-bind:key="sound")
</template>

<script>
import { sounds } from "~/contents/sounds.js";
import SoundButton from "~/components/soundboard/SoundButton.vue";

export default {
  components: { SoundButton },
  data: function() {
    return {
      sounds: sounds,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "~/layouts/styles/globals.scss";

.soundboard {
  padding: var(--dense-padding);
  background-color: var(--background-color);
  
  h2 {
    color: var(--text-color-dark);
    font-size: 1.5rem;
    @include phone-screen {
      font-size: 1.3rem;
    }
    margin-bottom: calc(var(--dense-padding) * 0.5);
  }
  .sounds {
    display: grid;
    // 170px
    grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));

    @include phone-screen {
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    }
    @include small-phone-screen {
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    }
    grid-gap: calc(var(--dense-padding) * 0.9);
  }
  // padding-bottom: var(--main-padding);
}
</style>
