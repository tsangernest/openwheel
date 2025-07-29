<template>
  <v-dialog
    :model-value="modelValue"
    persistent
    max-width="600"
  >
    <v-card>
      <v-card-item class="text-center">
        <v-card-title><h3>[ ! ] WARNING [ ! ]</h3></v-card-title>
        <v-card-subtitle>Warning this is a permanent ACTION!</v-card-subtitle>
      </v-card-item>

      <v-card-text class="text-center">
        Are you sure you want to delete
        <br>
        <strong>#{{ driver.number }} {{ driver.surname.toUpperCase() }}</strong>, {{ driver.forename }} ?

        <v-checkbox
          v-model="confirmToggle"
          class="ml-16 px-16"
          :label="`Yes, I want to delete ${driver.surname.toUpperCase()}`"
        />

        <v-text-field
          v-show="confirmToggle"
          v-model="confirmDeleteLastname"
          :hint="`Please enter ${driver.surname} to confirm`"
          persistent-hint
          density="compact"
          single-line
          min-width="300"
        />
      </v-card-text>

      <v-divider/>
      <v-card-actions class="bg-surface-light">
        <v-btn
          text="Delete"
          border
          :disabled="(!confirmToggle) + (confirmDeleteLastname !== `${driver.surname}`) "
          @click="deleteDriver"
        />
        <v-spacer/>
        <v-btn
          text="Cancel"
          border
          @click="closeRemoveVerificationDialog"
        />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>



<script>
import axios from 'axios'

export default {
  name: 'RemoveVerificationDialog',

  props: {
    modelValue: {
      type: Boolean,
      required: true,
    },
    driver: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      confirmToggle: false,
      confirmDeleteLastname: '',
    }
  },

  methods: {
    closeRemoveVerificationDialog() {
      this.confirmToggle = false
      this.confirmDeleteLastname = ''
      this.$emit('update:modelValue', false)
    },

    deleteDriver() {
      if(this.confirmDeleteLastname === `${this.driver.surname}`) {
        axios
          .delete(`/driver/${this.driver.id}/`)
          .then(response => {
            if(response.status === 204) {
              this.$emit('refreshDriversTable', {sortBy: ''})
              this.closeRemoveVerificationDialog()
            }
          })
          .catch(e => console.log(e))
      }
    },
  },
}

</script>

