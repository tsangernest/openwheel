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
          show-expand
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
                  @click="addDriver"
                />
              </template>
            </v-toolbar>
          </template>

          <template v-slot:item.data-table-expand="{ internalItem, isExpanded, toggleExpand }">
            <v-btn
              class="text-none"
              variant="text"
              :append-icon="isExpanded(internalItem) ? 'mdi-chevron-up': 'mdi-chevron-down'"
              @click="toggleExpand(internalItem)"
            />
          </template>

          <template v-slot:expanded-row="{ columns, item }">
            <tr>
              <td :colspan="columns.length">
                <v-sheet
                  rounded="lg"
                  border
                >
                  <v-table density="compact">
                    <tbody class="bg-surface-light">
                      <tr>
                        <th>Race Number</th>
                        <th>Date of Birth</th>
                        <th>Nationality</th>
                        <th>Wiki URL</th>
                      </tr>
                    </tbody>

                    <tbody>
                      <tr>
                        <td>{{ item.number }}</td>
                        <td>{{ item.date_of_birth }}</td>
                        <td>{{ item.nationality }}</td>
                        <td>{{ item.url }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </v-sheet>
              </td>
            </tr>
          </template>
        </v-data-table-server>

        <v-dialog
          v-model="showAddEditDialog"
          max-width="500"
          persistent
        >
          <v-card>
            <template v-slot:text>
              <v-row>
                <v-col>
                  <v-text-field
                    label="First name"
                    density="compact"
                  />
                </v-col>
                <v-col>
                  <v-text-field
                    label="Last name"
                    density="compact"
                  />
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <v-text-field
                    label="Reference"
                    density="compact"
                  />
                </v-col>
                <v-col>
                  <v-text-field
                    label="Code"
                    density="compact"
                  />
                </v-col>
                <v-col>
                  <v-text-field
                    label="Number"
                    density="compact"
                  />
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <v-text-field
                    label="Birthday"
                    density="compact"
                  />
                </v-col>
                <v-col>
                  <v-text-field
                    label="Country"
                    density="compact"
                  />
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <v-text-field
                    label="Wiki URL"
                    density="compact"
                  />
                </v-col>
              </v-row>
            </template>

            <v-spacer/>
            <v-divider/>

            <v-card-actions class="bg-surface-light">
              <v-btn
                text="Save"
                border
              />
              <v-spacer/>
              <v-btn
                text="Cancel"
                border
                @click="showAddEditDialog = false"
              />
            </v-card-actions>

          </v-card>
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
        { title: 'Code', key: 'code', sortable: false, width: 100 },
        { title: 'First Name', key: 'forename', sortable: true, nowrap: true, width: 1 },
        { title: 'Last Name', key: 'surname', sortable: true, nowrap: true },
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

    addDriver() {
      this.showAddEditDialog = true
    }
  },
}
</script>

