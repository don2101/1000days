<template>
<div>
<v-container>
<v-card>
<h1 class="headline"><strong>개인 정보 수정</strong></h1>
<v-card-text>
<v-container>
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
             <div v-if="this.editpassword!=this.editpasswordconfirm&& this.editpasswordconfirm.length>0">
              <p class="ml-3" style="color:red;">비밀번호가 일치하지 않습니다</p>
              </div>
              </v-col>
 </v-row>
 </v-container>
   <h6>계정 공개 여부 설정 *</h6>
  <div v-if="this.accountYN==true">
    <v-switch v-model="accountYN" :label="'공개'"></v-switch>
  </div>
  <div v-else>
    <v-switch v-model="accountYN" :label="'비공개'"></v-switch>
  </div>
  <h6>팔로우/팔로잉 공개 여부 설정 *</h6>
  <div v-if="this.followYN==true">
    <v-switch v-model="followYN" :label="'공개'"></v-switch>
  </div>
  <div v-else>
    <v-switch v-model="followYN" :label="'비공개'"></v-switch>
  </div>

            <v-card-actions>
                <v-btn style="left:90%" color="pink lighten-2" @click="edit()"><i class="material-icons">save_alt 저장</i></v-btn>
             </v-card-actions>
                </v-card-text>
 </v-card>
 </v-container>
</div>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: 'AccountPage',
     data: () => ({
      editname:'',
      editnickname:'',
      editemail:'',
      editpassword:'',
      editpasswordconfirm:'',
      accountYN: true,
      followYN: true,
      checkbox: false,
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

<style scoped>
.container{
   width: 100%;
   margin-top: 100px;
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
font-size:15px;
}

</style>