<template>
   <div class="container" style="margin-top:100px; margin-bottom: 100px;">
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >

          <v-card
            max-width="500"
            class="ml-5 mr-5 mt-5 mb-5"
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

        <v-btn color="red" text v-on="on"><v-icon>mdi-heart</v-icon>0</v-btn></v-btn>

        <v-btn color="blue" text v-on="on" data-toggle="modal" data-target="#Commentdetail"><v-icon>mdi-comment</v-icon>0</v-btn></v-btn>

<v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn @click="bell" color="yellow" text v-on="on"><i class="fas fa-bell fa-2x"></i></v-btn>
      </template>
      <span>신고</span>
    </v-tooltip>


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
        { title: 'Title', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6 },
        { title: '제목', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: '일기', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
        { title: '육아일기제목', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
    methods:{
    bell(){
        Swal.fire({
                  type: 'success',
                  text: '신고가 정상적으로 접수되었습니다',
        })
    }
  }
  }
</script>

<style scoped>

.container{
width:70%
}
h1{
color:#1E88E5;
text-align: center;
}


</style>