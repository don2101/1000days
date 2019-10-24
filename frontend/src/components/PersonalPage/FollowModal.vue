<template>
  <v-row justify="center">
    <!-- v-model에 store에서 받아온 isFollowModal 걸어주기 -->
    <v-dialog v-model="isFollowModal" scrollable persistent max-width="300px">
      <v-card>
        <v-card-title>Follower or Following</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
            팔로우 목록 반복문 돌면서 띄워 주기
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="toggleFM(false)">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
  import {mapActions, mapGetters} from 'vuex'
 export default {
     name:'FollowModal',
     data() {
         return {
           followers: [],
           followings: []
         }
     },
     computed: {
         // store에서 받아오기
       ...mapGetters('data', ['isFollowModal'])
     },
   methods: {
       ...mapActions('data', ['toggleFM'])
   }

 }
</script>

<style>

</style>