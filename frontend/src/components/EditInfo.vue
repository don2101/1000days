<template>
<div class="container" style="margin: auto">
 <v-btn color="primary" class="mr-3" style="float:right" @click="editinfo()">수정하기</v-btn>
<div v-if="show==true">
<h1 class="headline"><strong>개인 정보 수정</strong></h1>
<v-col cols="12" sm="6">
<v-text-field v-model="editname" :readonly="true" label="이름"></v-text-field>
</v-col>
<v-col cols="12" sm="6">
<v-text-field v-model="editnickname" :readonly="false" label="닉네임"></v-text-field>
 </v-col>
 <v-text-field v-model="editemail" :readonly="true" label="이메일"></v-text-field>
 <v-text-field v-model="editpassword" :readonly="false" label="비밀번호"></v-text-field>
 <v-text-field v-model="editpasswordconfirm" :readonly="false" label="비밀번호 확인"></v-text-field>
 <v-btn color="primary" class="mr-3" style="float:right" @click="edit()">저장</v-btn>
</div>
</div>
</template>


<script>
import {mapState} from 'vuex'
export default {
  name: 'AccountPage',
     data: () => ({
      show: false,
      editemail:'',
      editpassword:'',
    }),
   components: {
  },
  methods: {
    editinfo(){
        this.show = true
        this.editemail = this.userInfo.email
        this.editpassword = this.userInfo.password
    },
    edit(){
    alert('dd')
           this.$store.commit('setUserInfo',{
            'email': this.editemail ,
            'password': this.editpassword,
            });
    }
  },
   computed: {
    ...mapState({
        userInfo: state => state.moduleName.userInfo
        }),
        }
  }
</script>
<style>
</style>