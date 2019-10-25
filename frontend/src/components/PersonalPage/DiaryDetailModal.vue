<template>
    <v-row justify="center">
    <!-- v-model에 store에서 받아온 isFollowModal 걸어주기 -->
    <v-dialog v-model="DetailModal.data" scrollable persistent widtt="auto">
      <v-card>
        <v-card-title>제목제목제목제목</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
            다이어리 디테일 모달
            제목
            내용
            디데이
            글쓴이
            좋아요
            댓글
            등등등
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="setDetailModal({'data': false})">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
    import {mapGetters, mapActions} from 'vuex'
    export default {
        name: 'DiaryDetailModal',
        data() {
            return {

            }
        },
        methods: {
            ...mapActions('data', ['setDetailModal'])
        },
        computed: {
            ...mapGetters('data', ['DetailModal'])
        }
    }
</script>

<style>

</style>