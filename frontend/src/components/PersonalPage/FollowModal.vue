<template>
  <v-row justify="center">
    <v-dialog v-model="isFMon" scrollable max-width="300px">
      <v-card>
        <v-card-title>Follower or Following</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
            팔로우 목록 반복문 돌면서 띄워 주기
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" text>Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
 export default {
     name:'FollowModal',
     data() {
         return {
         }
     },
     computed: {
         // store에서 받아오기
         isFMon() {
             return false
         }
     },

 }
</script>

<style>

</style>