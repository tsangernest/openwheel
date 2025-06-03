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
                label="First name"
                density="compact"
              />
            </v-col>
            <v-col>
              <v-text-field
                label="last name"
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

export default {
  name: 'AddEditDriverDialog',

  data() {
    return {

    }
  },

  methods: {
    closeAddEditDriverDialog() {
      this.$refs.addEditDriverForm.reset()
      this.$emit('update:modelValue', false)
    },

    saveDriver() {
      console.log('In save driver')
    }

  },
}

</script>

