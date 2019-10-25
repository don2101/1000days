<template>
   <div class="container" style="margin-top:20px; margin-bottom: 100px;">
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >

          <v-card
            max-width="500"
            class=""
    >
            <v-img
             data-toggle="modal"
            data-target="#Diarydetail"
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>
             <v-card-actions>

        <button @click="favorite" text><i id="favorite" class="fas fa-heart"></i>0</button>

        <button class="ml-5" text v-on="on" data-toggle="modal" data-target="#Commentdetail"><i class="fal fa-comment-dots"></i>0</button>

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
         오늘은 돌잔치를 했다!!!!!!!
        </v-card-text>
      </div>
    </v-expand-transition>
          </v-card>
        </v-col>
       <DiaryDetail></DiaryDetail>
       <CommentDetail></CommentDetail>
      </v-row>

     <v-row dense>
        <v-col>
          <v-card
            @click="more"
            color="#E0E0E0"
            class="mt-1"
            >
              <v-card-text >
               <i class="fad fa-plus"></i>
              </v-card-text>
          </v-card>
        </v-col>
      </v-row>


    </div>
</template>

<script>
import DiaryDetail from'./DiaryDetail'
import CommentDetail from'./CommentDetail'
import Comment from'./Comment'
  export default {
    components:{
    DiaryDetail,
    CommentDetail,
    Comment
    },
    data: () => ({
    show:false,
       cards: [
        {src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 4 },
        {src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 4 },
        {src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 4 },
         {src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 4 },
        {src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 4 },
        {src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 4 },
      ],
    }),
    methods:{

    favorite(){
$("#favorite").css("color","red");
    },
    more(){
    }
  }
  }
</script>

<style scoped>

h1{
color:#1E88E5;
text-align: center;
}

button:focus{
outline: none;
}

.fa-heart:click{
color:red;
}

.fa-plus{
left:50%;
font-size:1.5rem
}
</style>