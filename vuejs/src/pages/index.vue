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

        <v-data-table
          :headers="driverHeaders"
          :items="drivers"
          density="compact"
        />

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
      drivers: [],

      // Driver table
      driverHeaders: [
        // { title: 'ID', key: 'id', align: 'start', sortable: false },
        { title: 'DriverRef', key: 'ref', alight: 'start', sortable: false },
        { title: 'Driver No.', key: 'number', sortable: false },
        { title: 'Code', key: 'code', sortable: false },
        { title: 'First Name', key: 'forename', sortable: true },
        { title: 'Last Name', key: 'surname', sortable: true },
        { title: 'Date of Birth', key: 'date_of_birth', sortable: true },
        { title: 'Nationality', key: 'nationality', sortable: true },
        // { title: 'Wiki URL', key: 'url', sortable: false },
      ],




      // Toggles
      showMobileMenu: false,

    }
  },

  components: {

  },

  mounted() {
    //this.getNationalities()
    this.getDrivers()
  },

  methods: {
    getDrivers() {
      axios
        .get('/driver')
        .then(response => { this.drivers = response.data.results; console.log(this.drivers); })
        .catch(e => console.log(e))
    }

    //getNationalities() {
    //  axios
    //    .get('/api/v1/driver')
    //    .then(response => {
    //      console.log(response)
    //      this.drivers = response.data
    //    })
    //    .catch(e => { console.error(e) })
    //}
  }
}
</script>

