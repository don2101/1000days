<template>
      <div class="container">
        <v-card>
          <h1 class="headline"><strong>회원 정보</strong></h1>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="이름 *" v-model="name" required>
              </v-col>
               <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="닉네임 *" v-model="nickname" required>
              </v-col>
               <v-col cols="12">
                <span class="icon"><v-icon middle>mdi-email</v-icon></span>
                 <input type="text" placeholder="이메일 *" v-model="newemail" required>
                </v-col>
               <v-col cols="12">
                 <span class="icon"><v-icon>fas fa-lock</v-icon></span>
                 <input type="password" placeholder="비밀번호 *" v-model="pw" required>
               </v-col>
               <v-col cols="12">
                 <span class="icon"><v-icon>fas fa-lock</v-icon></span>
                 <input type="password" placeholder="비밀번호 확인 *" v-model="repw" required>
               </v-col>
             <div v-if="this.pw!=this.repw&&this.repw.length>0">
              <p style="color:red;">비밀번호가 일치하지 않습니다</p>
              </div>
              </v-col>
            </v-row>

            <h6>계정 공개 여부 설정 *</h6>
              <div v-if="this.accountYN==true">
              <v-container fluid>
    <v-switch v-model="accountYN" :label="'공개'"></v-switch>
  </v-container>
  </div>
  <div v-else>
              <v-container fluid>
    <v-switch v-model="accountYN" :label="'비공개'"></v-switch>
  </v-container>
  </div>
  <h6>팔로우/팔로잉 공개 여부 설정 *</h6>
              <div v-if="this.followYN==true">
              <v-container fluid>
    <v-switch v-model="followYN" :label="'공개'"></v-switch>
  </v-container>
  </div>
  <div v-else>
              <v-container fluid>
    <v-switch v-model="followYN" :label="'비공개'"></v-switch>
  </v-container>
  </div>
   <h6>아기가 있습니까? *</h6>
              <div v-if="this.babyYN==true">
              <v-container fluid>
    <v-switch v-model="babyYN" :label="'있음'"></v-switch>
  </v-container>
  </div>
  <div v-else>
              <v-container fluid>
    <v-switch v-model="babyYN" :label="'없음'"></v-switch>
  </v-container>
  </div>
   </v-container>

            <div v-if="babyYN==true">
              <v-card
    max-width="344"
    class="mx-auto"
  >
  <h1 class="headline"><strong>아기 정보</strong></h1>
             <v-img
             src="../images/baby.png"
             height="150"
             width="150"
             class="mt-5"
             style="left:25%;"
           >
           </v-img>
           <v-card-text>
            <div style="margin-right:100px;">
               <v-col cols="12" style="left:25%">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="아기 이름" v-model="babyname">
              </v-col>
               <Calendar></Calendar>
                 <v-col cols="12" style="left:25%">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="배우자 이름" v-model="spousename">
              </v-col>

        </div>
        </v-card-text>
        </v-card>
        </div>
        </v-card-text>
        <br>
        <small><p style="text-align:center;">*필수입력항목</p></small>
        <small><p style="text-align:center;">*아직 아기가 태어나지 않은 경우 출산예정일을 입력해주세요 <br>(태어난 후 아기생일로 수정해주세요)</p></small>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="out">나가기</v-btn>
          <v-btn color="pink" text @click="register">가입하기</v-btn>
        </v-card-actions>
      </v-card>
    </v-card>
    </div>
</template>

<script>
import axios from 'axios';
import Calendar from './Calendar'
  export default {
    data: () => ({
      dialog: false,
      name: null,
      nickname: null,
      newemail:null,
      pw: null,
      repw: null,
      babyYN: true,
      babyname: null,
      spousename: null,
      accountYN: true,
      followYN: true,
    }),
    components:{
        Calendar
    },
    computed: {
     isValidate: function() {
      if (this.name === null || this.nickname === '' || this.newemail === null || this.pw === '' || this.repw === null)
        return false
      else return true
    }
    },

    methods: {
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
    register(){
    if (!this.isValidate) {
         Swal.fire({
                  type: 'error',
                  text: '모든 항목을 입력해주세요',
        })
      }
    if (this.pw != this.repw || this.pw.length<10 ){
        alert('비밀번호를 확인해주세요')
    }
    else {
    axios.post('http://localhost:8000/account/signup/', {
            "username": this.name,
            "password": this.pw,
            "email": this.newemail,
            "nickname": this.nickname,
            "select_baby": this.babyYN,
            "account_open": this.accountYN,
            "follower_open": this.followYN
        })
        .then(res => {
                        alert('회원가입 성공');
                        this.dialog = false

                    })
                    .catch(err => {
                        alert('회원가입 실패');
                        this.dialog = false
                    })

    }
  },
  }
  }
</script>

<style scoped>
.container{
   width: 70%;
}

h1{
color:#F8BBD0;
text-align: center;
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

</style>