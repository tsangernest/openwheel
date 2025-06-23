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
      </v-card-text>

      <v-checkbox
        v-model="confirmToggle"
        class="ml-16 px-16"
        :label="`Yes, I want to delete ${driver.surname.toUpperCase()}`"
      />
      <v-divider/>
      <v-card-actions class="bg-surface-light">
        <v-btn
          text="Delete"
          border
          :disabled="!confirmToggle"
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
// import axios from 'axios'

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
    }
  },

  methods: {
    closeRemoveVerificationDialog() {
      this.confirmToggle = false
      this.$emit('update:modelValue', false)
    },
  },
}

</script>

