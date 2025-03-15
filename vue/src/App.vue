<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link
          to="/"
          class="navbar-item"
        >
          <strong>OpenWheel</strong>
        </router-link>


        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"/>
          <span aria-hidden="true"/>
          <span aria-hidden="true"/>
        </a>
      </div>


      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log In</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>


    <section class="section">
      <router-view/>
    </section>


    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2025</p>
    </footer>
  </div>
</template>


<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma'
</style>

