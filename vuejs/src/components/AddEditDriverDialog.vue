<template>
  <v-dialog
    :model-value="modelValue"
    max-width="500"
    persistent
  >
    <v-card>
      <template v-slot:text>
        <v-form ref="addEditDriverForm">
          <v-row>
            <v-col>
              <v-text-field
                v-model="driverObj.forename"
                label="First name"
                density="compact"
              />
            </v-col>
            <v-col>
              <v-text-field
                v-model="driverObj.surname"
                label="last name"
                density="compact"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field
                v-model="driverObj.ref"
                label="Reference"
                density="compact"
              />
            </v-col>
            <v-col>
              <v-text-field
                v-model="driverObj.code"
                label="Code"
                density="compact"
              />
            </v-col>
            <v-col>
              <v-text-field
                v-model="driverObj.number"
                label="Number"
                density="compact"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field
                v-model="driverObj.date_of_birth"
                label="Birthday"
                density="compact"
                persistent-hint
                hint="Please enter yyyy-mm-dd"
              />
            </v-col>
            <v-col>
              <v-select
                v-model="driverObj.nationality"
                label="Country"
                density="compact"
                :items="nationalityItems"
                :item-value="'id'"
                :item-title="'country'"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field
                v-model="driverObj.url"
                label="Wiki URL"
                density="compact"
              />
            </v-col>
          </v-row>
        </v-form>
      </template>

      <v-spacer/>
      <v-divider/>

      <v-card-actions class="bg-surface-light">
        <v-btn
          text="Save"
          border
          @click="saveDriver"
        />
        <v-spacer/>
        <v-btn
          text="Cancel"
          border
          @click="closeAddEditDriverDialog"
        />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
import axios from 'axios'

export default {
  name: 'AddEditDriverDialog',

  props: {
    modelValue: {
      type: Boolean,
      required: true,
    },
    driverId: {
      default: 0,
      type: Number,
      required: false,
    },
  },

  data() {
    return {
      driverObj: {},
      nationalityItems: [],
    }
  },

  watch: {
    'driverId' () {
      if(this.driverId) {
        axios
          .get(`/driver/${this.driverId}/`)
          .then(response => { this.driverObj = response.data })
          .catch(e => console.log(e))
      }
    },
  },

  mounted() {
    this.getNationality()
  },

  methods: {
    closeAddEditDriverDialog() {
      this.$refs.addEditDriverForm.reset()
      this.driverObj = {}
      this.$emit('update:modelValue', false)
      this.$emit('update:driverId')
    },

    saveDriver() {
      let httpMethod = {
        method: this.driverId ? 'put': 'post',
        url: this.driverId ? `/driver/${this.driverId}/`: '/driver/',
        data: this.driverObj,
      }
      axios
        .request(httpMethod)
        .then(response => { if(response.status === 201 || response.status === 200) this.$emit('refreshDriversTable', {sortBy: ''}) })
        .catch(e => { console.log(e) })
        .finally(() => { this.closeAddEditDriverDialog() })
    },

    getNationality() {
      axios
        .get('/nationality/')
        .then(response => { this.nationalityItems = response.data })
        .catch(e => { console.log(e) })
    },
  },
}

</script>

