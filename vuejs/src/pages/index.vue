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
          v-model:items-per-page="itemsPerPage"

          :headers="driverHeaders"
          :items="drivers"
          :items-length="totalItems"
          :items-per-page-options="itemsPerPageOptions"

          :loading="driverTableLoading"
          @update:options="getDrivers"
          density="compact"
          hover
        >

        </v-data-table-server>

        <v-dialog
          v-model="showAddEditDialog"
          max-width="600"
        >

        </v-dialog>

        <section class="section">
          <router-view/>
        </section>

        <v-spacer/>
        <v-card>
          <vue-dropzone
            :options="dropzoneOptions"
          />

        </v-card>

        <footer class="footer">
          <p class="has-text-centered">Copyright (c) 2025</p>
        </footer>

      </div>
    </v-container>
  </v-app>
</template>




<script>
import axios from 'axios'
import vueDropzone from 'dropzone-vue3'

export default {
  name: 'Index',

  components: {
    vueDropzone,
  },

  data() {
    return {
      // * BEGIN Driver table *
      driverTableLoading: false,
      driverHeaders: [
        //{ title: 'ID', key: 'id', align: 'start' },
        //{ title: 'DriverRef', key: 'ref', alight: 'start', sortable: false },
        //{ title: 'Driver No.', key: 'number', sortable: false },
        { title: 'Code', key: 'code', sortable: false, width: 100 },
        { title: 'First Name', key: 'forename', sortable: true, nowrap: true, width: 1 },
        { title: 'Last Name', key: 'surname', sortable: true, nowrap: true },
        //{ title: 'Date of Birth', key: 'date_of_birth', sortable: true },
        //{ title: 'Nationality', key: 'nationality', sortable: true },
        // { title: 'Wiki URL', key: 'url', sortable: false },
      ],
      itemsPerPageOptions: [5, 10, 25, 100],
      drfParams: {},
      // * END Drivers Table *

      // * BEGIN Dropzone *
      dropzoneOptions: {
        url: 'http://localhost:8000/upload',
        thumbnailWidth: 30,
        maxFilesize: 3,
        //headers: { 'Content-Type': 'application/json' },
      },
      // * END dropzone *

      // Toggles
      showMobileMenu: false,
      showAddEditDialog: false,
    }
  },

  methods: {
    getDrivers({ page, itemsPerPage, sortBy }) {
      this.driverTableLoading = true

      if(sortBy.length > 0) {
        let sortDirection = sortBy[0].order === 'asc' ? '' : '-'
        this.drfParams['ordering'] = `${sortDirection}${sortBy[0].key}`
      }
      this.drfParams['page'] = page
      this.drfParams['page-size'] = itemsPerPage

      axios
        .get('/driver', { params: { ...this.drfParams } } )
        .then(response => { this.processPagination(response.data) })
        .catch(e => console.log(e))
        .finally(() => { this.driverTableLoading = false })
    },

    processPagination(data) {
      this.totalItems = data['count']
      this.drivers = data['results']
    },
  },
}
</script>

