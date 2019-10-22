<template>
   <div class="container">
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >

          <v-card
            max-width="500"
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
<v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn color="red" text v-on="on"><v-icon>mdi-heart</v-icon></v-btn></v-btn>
      </template>
      <span>좋아요</span>
    </v-tooltip>


<v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn color="blue" text v-on="on"><v-icon>mdi-comment</v-icon></v-btn></v-btn>
      </template>
      <span>댓글</span>
    </v-tooltip>

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
      </v-row>
    </div>
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

<style>

.container{
width:70%
}
h1{
color:#1E88E5;
text-align: center;
}


</style>