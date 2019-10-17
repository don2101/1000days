<template>
<div class="container">
<div class="row">
  <div class="col-3">
    <h1>My Page</h1>
    <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link" id="v-pills-home-tab" data-toggle="pill" @click="editinfo()" role="tab" aria-selected="false">회원정보</a>
      <a class="nav-link active" id="v-pills-profile-tab" data-toggle="pill" @click="remove()" role="tab" aria-selected="true">회원탈퇴</a>
    </div>
  </div>
</div>
<div v-if="show==true">
<h1 class="headline"><strong>개인 정보 수정</strong></h1>
 <v-row>
              <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="이름" v-model="editname" required>
              </v-col>
               <v-col cols="12">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="닉네임" v-model="editnickname" required>
              </v-col>
               <v-col cols="12">
                <span class="icon"><v-icon middle>mdi-email</v-icon></span>
                 <input type="text" placeholder="이메일" v-model="editemail" required readonly>
                </v-col>
               <v-col cols="12">
                 <span class="icon"><v-icon>fas fa-lock</v-icon></span>
                 <input type="password" placeholder="비밀번호" v-model="editpassword" required>
               </v-col>
               <v-col cols="12">
                 <span class="icon"><v-icon>fas fa-lock</v-icon></span>
                 <input type="password" placeholder="비밀번호 확인" v-model="editpasswordconfirm" required>
               </v-col>
             <div v-if="this.editpassword!=this.editpasswordconfirm">
              <p class="ml-3" style="color:red;">비밀번호가 일치하지 않습니다</p>
              </div>
              </v-col>
 </v-row>
  <v-radio-group class="select"v-model="accountYN" :mandatory="false">
              <h6>계정 공개 여부 설정</h6>
              <br>
              <v-radio label="공개" value="accountY"></v-radio>
              <v-radio label="비공개" value="accountN"></v-radio>
            </v-radio-group>
        <v-radio-group class="select" v-model="followYN" :mandatory="false">
              <h6>팔로우/팔로잉 공개 여부 설정</h6>
              <br>
              <v-radio label="공개" value="followY"></v-radio>
              <v-radio label="비공개" value="followN"></v-radio>
            </v-radio-group>
  <v-btn color="pink"style="float:right" @click="edit()"><i class="material-icons">save_alt 저장</i></v-btn>
</div>
<div  v-if="show==false">
<p>탈퇴 안내</p>
사용하고 계신 아이디는 탈퇴할 경우 재사용 및 복구가 불가능합니다.
탈퇴 후 회원정보는 모두 삭제됩니다
<v-btn color="red"style="float:right" @click="edit()">탈퇴</v-btn>
</div>
</div>
</template>


<script>
import {mapState} from 'vuex'
export default {
  name: 'AccountPage',
     data: () => ({
      show: false,
      editname:'',
      editnickname:'',
      editemail:'',
      editpassword:'',
      editpasswordconfirm:'',
      accountYN: 'accountY',
      followYN: 'followY'
    }),
   components: {
  },
  methods: {
    remove(){
        this.show = false
    },
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

<style scoped>
.container{
   width: 70%;
}

h1{
color:#F8BBD0;
text-align: center;
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

.icon{
  position: absolute;
  top: 15%;
  margin-left: 17px;
  margin-top: 17px;
  z-index: 1;
  color: #4f5b66;
}

.material-icons{
color:#fff;
}
</style>