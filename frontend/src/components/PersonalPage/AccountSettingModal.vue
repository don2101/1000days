<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="isASMon" scrollable max-width="300px">
          <v-card>
            <v-card-title>계정 설정</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="height: 300px;">
                프로필 사진 바꾸기
                계정 공개/비공개
                팔로우 공개/비공개
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn color="blue darken-1" text>Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </div>
</template>

<script>
    export default {
        name: 'AccountSettingModal',
        data() {
            return {

            }
        },
        computed: {
            // store에서 가져와서 뱉어주기
            isASMon() {
                return false
            }
        }
    }
</script>

<style>

</style>