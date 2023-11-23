<template>
    <v-main class="d-flex align-center  flex-column " style="min-height: 300px;">
      <v-container class="bg-background" id="orderContainer" >
        <v-row cols="12" >
        <v-col sm="4"></v-col>
        <v-col class="justify-center"  sm="6">
      <div class="text-h5">Dania Obiadowe</div>
      <v-dialog width="25%" v-for="item in items" :key="item.title" display="inline-block" persistent  class="align-self-md-center">
  <template v-slot:activator="{ props }">
    <v-card v-bind="props" :text="item.title" height="200" :elevation="8"  class="ma-3 pa-3 text-center d-flex" >
      <v-img
      width="100" height="200"
      cover
      :src="require('@/assets/' + item.icon +'.jpg')"></v-img>
    </v-card>
  </template>

  <template v-slot:default="{ isActive }" >
    <v-card class="justify-center mt-auto"  :title="item.title"  :elevation="8">
      <v-img
        height="500"
        width="1000"
        :src="require('@/assets/' + item.icon +'.jpg')"
        ></v-img>
      <v-card-text>
        zawiera alergeny:
      </v-card-text>
      <v-card-text>
        kurczak, ryż
      </v-card-text>
      <v-card-text>
        Cena 15zl
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          text="Zamknij"
          @click="isActive.value = false"
        ></v-btn>
        <v-btn
          text="Zamów"
          @click="isActive.value = false"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
<!--######################################-->
<v-dialog width="25%" v-for="item in items" :key="item.title" display="inline-block" persistent  class="align-self-md-center">
  <template v-slot:activator="{ props }">
    <v-card v-bind="props" :text="item.title" height="200" :elevation="8"  class="ma-3 pa-3 text-center d-flex" >
      <v-img
      width="100" height="200"
      cover
      :src="require('@/assets/' + item.icon +'.jpg')"></v-img>
    </v-card>
  </template>

  <template v-slot:default="{ isActive }" >
    <v-card class="justify-center mt-auto"  :title="item.title"  :elevation="8">
      <v-img
        height="500"
        width="1000"
        :src="require('@/assets/' + item.icon +'.jpg')"
        ></v-img>
      <v-card-text>
        zawiera alergeny:
      </v-card-text>
      <v-card-text>
        kurczak, ryż
      </v-card-text>
      <v-card-text>
        Cena 15zl
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          text="Zamknij"
          @click="isActive.value = false"
        ></v-btn>
        <v-btn
          text="Zamów"
          @click="isActive.value = false"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
</v-col>
<v-col sm="4"></v-col>
</v-row>
</v-container>
    </v-main>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomePage',

  data () {
    return {
      menu: ['zamów', 'ustawienia'],
      items: [
        { icon: 'chicken', title: 'Kurczak z ryżem', description: 'kurczak ryż' },
        { icon: 'fish', title: 'Ryba z frytkami', description: 'Ryba, frytki' },
        { icon: 'placek', title: 'Placek po Węgiersku', description: 'Placek, Węgier' }
      ]
    }
  },
  methods: {
  }
})
</script>
<style scoped>
.v-col-sm-4{
  flex:1 !important;
}
.bg-background{
  background: rgba(255,255,255,0.6) !important;
  width:60% !important;
  max-height:"100vh" !important;
  overflow-y: scroll;
}
#orderContainer{
  margin-top:15px;
  height: 100vh;
}
</style>
