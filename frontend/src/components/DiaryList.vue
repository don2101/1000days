<template>

    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>
            <v-card-text>
            시간 역순으로 출력</br>
            작성자 이름(클릭시 작성자 개인 페이지로 이동)<br>
            d+day 출력<br>
            좋아요, 댓글 기능<br>
            댓글 작성자 클릭시 작성자 개인 페이지로 이동<br>
            신고 기능
            <i class="fas fa-bell"></i>
            <br>
            육아일기 내용
            <v-btn style="float:right;" color="orange" @click="readmore()">더보기</v-btn>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>

              <v-btn icon>
                <v-icon>mdi-bookmark</v-icon>
              </v-btn>

              <v-btn icon>
                <v-icon>mdi-message-text</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
  export default {
    data: () => ({
      cards: [
        { title: '육아일기 제목', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6 },
        { title: '육아일기 제목', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: '육아일기 제목', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
  }
</script>

<style>

h1{
color:#1E88E5;
text-align: center;
}

</style>