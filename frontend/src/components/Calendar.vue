<template>
  <v-row>
    <v-col
      cols="12"
      style="left:180%;"
    >
      <v-menu
        ref="nowMenu"
        v-model="nowMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="now"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="now"
            label="아기 생년월일"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="now"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="nowMenu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.nowMenu.save(now)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
  </v-row>
</template>
<script>

  export default {
    data: () => ({
      nowMenu: false,
      now: null,
    }),
    computed: {
    },
    methods: {
    },
  }
</script>
<style scoped>
</style>