<template>
  <div>
    <Navbar />
    <section class="section">
      <div class="container">
        <router-view />
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue'
import axios from 'axios';
export default {
  name: 'App',
  components: {
    Navbar
  },
  beforeCreate(){
    this.$store.commit('initialiseStore')
    if (this.$store.state.token) {
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    }else {
      axios.defaults.headers.common['Authorization'] = null
    }
  }
}
</script>
<style lang="scss">
@import '../node_modules/bulma';
</style>
