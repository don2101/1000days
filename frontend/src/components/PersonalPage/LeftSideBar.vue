<template>
  <v-card
    class="mx-auto"
    width="256"
    tile
    style="z-index: 100;"
  >
    <v-navigation-drawer v-model="drawer"
      :mini-variant.sync="mini" permanent>

      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="../../images/Babies/sleepingBaby.jpg"></v-img>
          </v-list-item-avatar>
          <div>{{loginedUserInfo.username}}</div>

        </v-list-item>
        

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">디데이</v-list-item-title>
            <v-list-item-subtitle>아기이름</v-list-item-subtitle>
          </v-list-item-content>

          <!-- 아기가 여러명일 경우 활성화 -->
          <!-- 아기를 선택해서 바꿀 경우 아기 이름, 디데이, 개인페이지의 내용, 아기정보가 다 바뀌어야함-->
          <v-list-item-action>
            <v-icon>mdi-menu-down</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <div :style="mini ? 'margin-left: 30%' : 'margin-left: 80%'">
            <v-btn
              icon
              @click.stop="mini = !mini"
            >
          <v-icon>{{mini ? 'mdi-chevron-right' : 'mdi-chevron-left'}}</v-icon>
        </v-btn></div>
      <v-list nav dense>
        <v-list-item-group v-model="item" color="primary">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>


<script>
  import {mapGetters} from 'vuex'
  export default {
    data() {
      return {
        item: 0,
        items: [
        { text: 'My Files', icon: 'mdi-folder' },
        { text: 'Shared with me', icon: 'mdi-account-multiple' },
        { text: 'Starred', icon: 'mdi-star' },
        { text: 'Recent', icon: 'mdi-history' },
        { text: 'Offline', icon: 'mdi-check-circle' },
        { text: 'Uploads', icon: 'mdi-upload' },
        { text: 'Backups', icon: 'mdi-cloud-upload' },
      ],
      drawer: true,
      mini: true,
      }
    },
    computed: {
      ...mapGetters('data', ['loginedUserInfo'])
    }
  }
</script>