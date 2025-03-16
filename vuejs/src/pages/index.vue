<template>
  <v-app>
    <v-container>
      <div id="wrapper">
        <nav class="navbar is-dark">
          <div class="navbar-brand">
            <router-link
              to="/"
              class="navbar-item"
            >
              <strong>openwheel</strong>
            </router-link>

            <a
              class="navbar-burger"
              aria-label="menu"
              aria-expanded="false"
              data-target="navbar-menu"
              @click="showMobileMenu = !showMobileMenu"
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div
            class="navbar-menu"
            id="navbar-menu"
          >
            <div class="navbar-end">
              <div class="navbar-item">
                <div class="buttons">
                  <router-link
                    to="/log-in"
                    class="button is-light"
                  >
                    Log In
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <v-data-table/>

        <section class="section">
          <router-view/>
        </section>

        <footer class="footer">
          <p class="has-text-centered">Copyright (c) 2025</p>
        </footer>

      </div>
    </v-container>
  </v-app>
</template>



<script>
import axios from 'axios'

export default {
  name: 'Index',

  data() {
    return {
      // Data from eps
      nationalities: [],


      // Toggles
      showMobileMenu: false,
    }
  },

  components: {

  },

  mounted() {
    this.getNationalities()
  },
  methods: {
    getNationalities() {
      axios
        .get('')
        .then(response => {
          console.log(response)
        })
        .catch(e => { console.error(e) })
    }
  }
}
</script>

