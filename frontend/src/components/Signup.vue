<template>
      <div style="margin-top:100px; margin-bottom: 100px;" class="container">
        <v-card>
          <h1>User Information</h1>
          <v-container>
            <v-row>
              <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="fad fa-id-card"></i></span>
                <input type="text" placeholder="이름 *" v-model="name" required>
              </v-col>
               <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="fad fa-id-card"></i></span>
                <input type="text" placeholder="닉네임 *" v-model="nickname" required>
              </v-col>
               <v-col cols="12">
                <span class="icon"><i style="font-size:1.5rem" class="fad fa-envelope"></i></span>
                 <input type="text" placeholder="이메일 *" v-model="newemail" required>
                </v-col>
               <v-col cols="12">
                 <span class="icon"><i class="fad fa-lock" style="font-size:1.5rem"></i></span>
                 <input type="password" placeholder="비밀번호 *" v-model="pw" required>
               </v-col>
              <p class="ml-2" style="color:green;">{{PW}}</p>
               <v-col cols="12">
                 <span class="icon"><i class="fad fa-lock" style="font-size:1.5rem"></i></span>
                 <input type="password" placeholder="비밀번호 확인 *" v-model="repw" required>
               </v-col>
             <p class="ml-2" style="color:red;">{{PWCheck}}</p>
              </v-col>
            </v-row>
            <v-col cols="12">
            <h6>계정 공개 여부 설정 *</h6>
              <div v-if="this.accountYN==true">
    <v-switch v-model="accountYN" :label="'공개'"></v-switch>
  </div>
  <div v-else>
    <v-switch v-model="accountYN" :label="'비공개'"></v-switch>
  </div>
  </v-col>
  <v-col cols="12">
  <h6>팔로우/팔로잉 공개 여부 설정 *</h6>
              <div v-if="this.followYN==true">
    <v-switch v-model="followYN" :label="'공개'"></v-switch>
  </div>
  <div v-else>
    <v-switch v-model="followYN" :label="'비공개'"></v-switch>
  </div>
  </v-col>
  <v-col cols="12">
   <h6>아기가 있습니까? *</h6>
              <div v-if="this.babyYN==true">
    <v-switch v-model="babyYN" :label="'있음'"></v-switch>
  </div>
  <div v-else>
    <v-switch v-model="babyYN" :label="'없음'"></v-switch>
  </div>
  </v-col>
   </v-container>
        <br>
        <small><p style="text-align:center;">*필수입력항목</p></small>
        <v-card-actions>
          <v-spacer></v-spacer>
          <div v-if="babyYN==false">
          <v-btn class="move" color="blue darken-1" text @click="out"><i class="mr-2 fad fa-sign-out-alt"></i>나가기</v-btn>
          <v-btn class="move" color="pink" text @click="register"><i class="mr-2 fad fa-user-plus"></i>가입하기</v-btn>
        </div>
        <div v-else>
        <v-btn class="move" color="blue darken-1" text @click="out"><i class="mr-2 fad fa-sign-out-alt"></i>나가기</v-btn>
          <v-btn class="move" color="pink" text @click="next">아기 정보 입력하기</v-btn>
        </div>
        </v-card-actions>
      </v-card>
    </v-card>
    </div>
</template>

<script>
import axios from 'axios';
import {mapState, mapGetters, mapActions} from 'vuex';
  export default {
    data: () => ({
      dialog: false,
      name: null,
      nickname: null,
      newemail:null,
      pw: null,
      repw: null,
      babyYN: true,
      accountYN: true,
      followYN: true,
    }),
    components:{
    },
    computed: {
    PW(){
     var passwordRules = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,16}$/;
        var password = this.pw;
    if (passwordRules.test(password)==false){
    return ('10-15자 영문자, 숫자, 특수기호의 조합을 사용해주세요')
    }
    else{
    return('사용가능')
    }
    },
    PWCheck(){
    if (this.pw!=this.repw&&this.repw!=null){
        return ('비밀번호가 일치하지 않습니다')
    }
    },
    userInfo() {
        return this.$store.state.data.auth.signupInfo
        },
        ...mapGetters(
        'auth', ['signupInfo']
    ),
     isValidate: function() {
      if (this.name === null || this.nickname === '' || this.newemail === null || this.pw === '' || this.repw === null)
        return false
      else return true
    }
    },
    methods: {
    ...mapActions('auth', ['savenickname']),
    out(){
     Swal.fire({
  title: '이 페이지에서 나가시겠습니까?',
  text: "작성하신 내용은 저장되지 않습니다",
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: '나가기',
  cancelButtonText: '취소'
}).then((result) => {
  if (result.value) {
    this.$router.push({
        name: 'HomePage'
    })
  }
})
    },
     next(){
    if (!this.isValidate) {
         Swal.fire({
                  type: 'error',
                  text: '모든 항목을 입력해주세요',
        })
      }
    else {
    var passwordRules = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,16}$/;
        var password = this.pw;
    if (this.pw != this.repw||passwordRules.test(password)==false){
       Swal.fire({
                  type: 'error',
                  text: '비밀번호는 숫자, 영문자, 특수문자의 조합으로 10~15자리를 사용해야 합니다'
        })
    }
    else{
    axios.post('http://localhost:8000/account/signup/', {
            "username": this.name,
            "password": this.pw,
            "email": this.newemail,
            "nickname": this.nickname,
            "select_baby": this.babyYN,
            "account_open": this.accountYN,
            "follower_open": this.followYN
        })
        .then(res=>this.savenickname(this.nickname))
        .then(res=> this.$router.push('/babyinfo'))

                    .catch(err => {
                         Swal.fire({
                 type: 'error',
                 text: '회원가입 실패',
       })
                        this.dialog = false
                    })
    }
    }
  },
    register(){
    if (!this.isValidate) {
         Swal.fire({
                  type: 'error',
                  text: '모든 항목을 입력해주세요',
        })
}
    else {
     var passwordRules = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,16}$/;
        var password = this.pw;
    if (this.pw != this.repw||passwordRules.test(password)==false){
       Swal.fire({
                  type: 'error',
                  text: '비밀번호는 숫자, 영문자, 특수문자의 조합으로 10~15자리를 사용해야 합니다'
        })
    }
    else{
    axios.post('http://localhost:8000/account/signup/', {
            "username": this.name,
            "password": this.pw,
            "email": this.newemail,
            "nickname": this.nickname,
            "select_baby": this.babyYN,
            "account_open": this.accountYN,
            "follower_open": this.followYN
        })
        .then(res=>this.$store.commit('setNicknameInfo', {
          'nickname' : this.nickname,
        }))
        .then(res => {
                        Swal.fire({
                  type: 'success',
                  text: '회원가입이 완료되었습니다',
        })
        .then(res=> this.$router.push('/login'))
                    })
                    .catch(err => {
                        alert('회원가입 실패');
                        this.dialog = false
                    })
    }
  }
  },
  }
  }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Chewy&display=swap');
.container{
    width:70%
}
h1{
color:#F8BBD0;
text-align: center;
font-family: 'Chewy', cursive;
}
.ml-3{
  color: #fff;
  padding: 12px 20px;
  margin: 20px 0;
  border: none;
  cursor: pointer;
  width: 95%;
}
.ml-3:focus{
outline: none;
}
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
h6{
  font-weight: bold;
  margin-right:10px;
}
.icon{
  position: absolute;
  top: 15%;
  margin-left: 17px;
  margin-top: 17px;
  z-index: 1;
  color: #4f5b66;
}
.select{
margin-left: 120px;
}

.move{
font-family: 'Jua', sans-serif;
font-size: 15px;
}
</style>