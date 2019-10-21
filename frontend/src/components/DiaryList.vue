<template>
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >

          <v-card
            class="mx-auto"
            max-width="500"
    >
            <v-img
             data-toggle="modal"
            data-target="#exampleModalCenter"
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>
             <v-card-actions>
      <v-btn
        color="red"
        text
      ><v-icon>mdi-heart</v-icon></v-btn>

      <v-btn
        color="blue"
        text
      >
<v-icon>mdi-comment</v-icon></v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
         육아일기 내용 /////
        </v-card-text>
      </div>
    </v-expand-transition>
          </v-card>
        </v-col>
        <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
      <h5 class="modal-title" id="exampleModalLongTitle">lemon</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
      <v-layout wrap>
        <v-flex xs12 sm6>
            <v-img
              src="https://jira.ssafy.com/secure/useravatar?avatarId=10339&s=48"
              height="100%"
              width="100%"
              style="align-items: flex-end; margin: auto;"
            ></v-img>
        </v-flex>
         <v-flex xs12 sm6>
         <div class="date">2019-10-21</div>
         <br>
            오늘은 돌잔치를 했다!!!!!!!!!!!!!!
        </v-flex>
        </v-layout>
      </div>
       <div class="modal-body">
      <Comment></Comment>
      </div>
    </div>
  </div>
</div>
      </v-row>
    </v-container>
</template>

<script>
import DiaryDetail from'./DiaryDetail'
import Comment from'./Comment'
  export default {
    components:{
    DiaryDetail,
    Comment
    },
    data: () => ({
    show:false,
       cards: [
        { title: 'title', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6 },
        { title: '제목', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: '육아일기제목', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
    methods:{
  }
  }
</script>

<style>

h1{
color:#1E88E5;
text-align: center;
}


</style>