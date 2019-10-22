<template>
  <v-row>
    <v-col
      cols="12"
    >
      <v-menu
        ref="nowMenu"
        v-model="nowMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="birthday"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
            <v-col cols="12" style="left:25%">
            <span class="icon"><i class="fas fa-calendar-week" style="font-size: 1.5em"></i></span>
                <input v-model="birthday" v-on="on" type="text" placeholder="아기 생년월일" readonly >
            </v-col>
        </template>
        <v-date-picker
          v-model="birthday"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="nowMenu = false"
          >
            취소
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.nowMenu.save(birthday)"
          >
            선택
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
      birthday: null,
    }),
    computed: {
    },
    methods: {
    },
  }
</script>
<style scoped>
input{
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  box-sizing: border-box;
  background-color: #EEEEEE;
  padding-left: 50px;
  transition: 1s;
}

input:focus{
outline: none;
border-color:#F8BBD0;
box-shadow: 0 0 8px 0 #F8BBD0;
}

input::placeholder {
  font-weight: bold;
}

.icon{
  position: absolute;
  top: 15%;
  margin-left: 17px;
  margin-top: 17px;
  z-index: 1;
  color: #4f5b66;
  transition: 1s;
}
</style>