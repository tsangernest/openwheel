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

        <v-data-table-server
          :headers="driverHeaders"
          :items="drivers"

          v-model:items-per-page="itemsPerPage"

          :items-length="totalItems"
          :items-per-page-options="itemsPerPageOptions"

          @update:options="getDrivers"

          :loading="driverTableLoading"
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

      driverTableLoading: false,
      // Driver table
      driverHeaders: [
        { title: 'ID', key: 'id', align: 'start' },
        { title: 'DriverRef', key: 'ref', alight: 'start', sortable: false },
        { title: 'Driver No.', key: 'number', sortable: false },
        { title: 'Code', key: 'code', sortable: false },
        { title: 'First Name', key: 'forename', sortable: true },
        { title: 'Last Name', key: 'surname', sortable: true },
        { title: 'Date of Birth', key: 'date_of_birth', sortable: true },
        { title: 'Nationality', key: 'nationality', sortable: true },
        // { title: 'Wiki URL', key: 'url', sortable: false },
      ],

      itemsPerPage: 10,
      itemsPerPageOptions: [5, 10, 25, 100, -1],
      sortBy: 'id',
      totalItems: 0,

      drfParams: {},

      // Toggles
      showMobileMenu: false,
    }
  },

  methods: {
    getDrivers() {
      this.driverTableLoading = true

      this.drfParams['page-size'] = this.itemsPerPage
      this.drfParams['ordering'] = this.sortBy

      axios
        .get('/driver', { params: { ...this.drfParams } } )
        .then(response => { this.processPagination(response.data) })
        .catch(e => console.log(e))
        .finally(() => { this.driverTableLoading = false })
    },

    processPagination(data) {
      console.log(data)

      this.totalItems = data['count']
      this.drivers = data['results']


      // * END *
      console.log("\nEND handlePagination")
      console.log("%o=", this.itemsPerPage)
      console.log("%o=", this.totalItems)
      console.log("%o=", this.sortBy)
    },
  },
}
</script>

