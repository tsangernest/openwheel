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
          hover
        >
          <template v-slot:top>
            <v-toolbar flat>
              <template v-slot:append>
                <v-btn
                  text='Add a driver'
                  prepend-icon='mdi-plus'
                  border
                  rounded='xl'
                  @click="showAddEditDialog = true"
                />
              </template>
            </v-toolbar>
          </template>

          <template v-slot:item.actions="{ item }">
            <div class="justify-end">
              <v-btn
                border
                size="small"
                icon="mdi-pencil"
                @click="editDriver(item)"
              />

              <v-btn
                border
                size="small"
                icon="mdi-delete"
                @click="removeDriver(item)"
              />
            </div>
          </template>

        </v-data-table-server>

        <add-edit-driver-dialog
          v-model="showAddEditDialog"
        />

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
import AddEditDriverDialog from '../components/AddEditDriverDialog'

export default {
  name: 'Index',

  components: {
    AddEditDriverDialog,
    vueDropzone,
  },

  data() {
    return {
      // * BEGIN Driver table *
      driverTableLoading: false,
      driverHeaders: [
        { title: 'Code', key: 'code', sortable: false, align: 'start', width: 100 },
        { title: 'First Name', key: 'forename', sortable: true, nowrap: true, width: 1 },
        { title: 'Last Name', key: 'surname', sortable: true, nowrap: true },
        { title: 'Actions', key: 'actions', sortable: false, align: 'end', nowrap: true },
      ],
      itemsPerPageOptions: [5, 10, 25, 100],
      drfParams: {},
      // * END Drivers Table *

      // * BEGIN Dropzone *
      dropzoneOptions: {
        url: 'http://localhost:8000/upload',
        thumbnailWidth: 30,
        maxFilesize: 3,
      },
      // * END dropzone *

      // Toggles
      showMobileMenu: false,
      showAddEditDialog: false,
    }
  },

  methods: {
    editDriver(item) {
      console.log('-editDriver-\n', JSON.stringify(item))


    },

    removeDriver(item) {
      // This doesn't actually remove anything right now
      console.log('-removeDriver-\n', JSON.stringify(item))
    },

    customToggleExpand(item) {
      console.log(JSON.stringify(item))
    },

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

