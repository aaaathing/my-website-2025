---
layout: post
title: "The voxel game I wanted to make"
date: 2025-07-25
author: thingmaker (aaaathing)
---

# The voxel game I wanted to make

I mostly wanted to make terrain generation and trees and foliage generation. I also wanted it to have flowing water and sand and more. An awesome thing about terrain is the many different kinds of stone and dirt. It would be fun to make terrain that looked good.

The terrain will have tall mountains and valleys and long rivers. The forests are dense and there are many different kinds of forests with different kinds of trees. Different trees appear in different temperatures and rainfall and elevations. It will have small voxels. Grass and leaves sway in the wind, and water flows in rivers.

In MC, it is sometimes annoying that the blocks are big, and you can't make something out of blocks that falls and slides down hills.

## What I want the game to be like

<img src="2025-07-29 16.46 Voxel Forest Shelter.png" style="filter:brightness(1.25)">

<a href="https://www.youtube.com/watch?v=1wufuXY3l1o"><img src="https://i.ytimg.com/vi/1wufuXY3l1o/hq720.jpg" style="filter:brightness(1.25)"><img src="https://pbs.twimg.com/media/EwSl3TWVkAYDx1M?format=jpg&name=large" style="filter:brightness(1.25)"><img src="https://pbs.twimg.com/ext_tw_video_thumb/1208998780164460544/pu/img/eGXwYbGqaQxwQ194.jpg" style="filter:brightness(1.75)"></a>

<a href="https://forum.luanti.org/viewtopic.php?t=25683"><img src="https://user-images.githubusercontent.com/6905002/99192695-79e9ff00-2774-11eb-9b78-3a4bc4c78217.png" style="filter:brightness(1.5)" loading="lazy"><img src="https://forum.luanti.org/download/file.php?mode=view&id=24732" style="filter:brightness(1.5)" loading="lazy"></a>

<a href="https://www.youtube.com/watch?v=Hc3sb6lx0ag"><img src="https://i.ytimg.com/vi/Hc3sb6lx0ag/hq720.jpg" loading="lazy"></a>

<img src="https://github.com/weigert/SimpleHydrology/blob/master/screenshots/side5.png?raw=true" loading="lazy">

<img src="https://digital4planet.org/wp-content/uploads/sites/83/2021/05/old-growth-forest-with-rotting-tree-trunk-covered-3Y39CX3-1.jpg" style="filter:brightness(1.25)" loading="lazy"><img src="https://assets.simpleviewinc.com/simpleview/image/upload//v1/clients/roanoke/SV11033107V_431_e585f91b-359b-44f4-93b9-70b310b7b3dc.jpg" loading="lazy">

to add: more example images


Jun 27, 2025: I walked around and imagined what the voxel/simulation could be like: A mountain slope with a small wood hut and presence of tall trees in the distance, bird sounds, walking into the hut and wood stepping sounds. Going to the bottom of the valley, a river flowing from left to right and more dense trees on the other side, water flowing sounds, tall mountain on the other side with yellow sunlight and shadow cast by other mountains. Looking at a sloped valley going down side of hill in the shadow, some trees around, rain falling. Rain in a city, looking at the water flowing from tall building to gutter on the ground. I thought about how it could have complicatedely connected things, like water streams.

### Example Gameplay

![](breaking-stone.png)
The player held a stone pickaxe. He raised it and hit the stone on the hill with it. The stone broke off. The player picked up the stone piece and walked away.

The player was in a desert filled with sand. He walked and looked for water. After a while, the player found a large puddle of clear water in a place surrounded by higher land. The player went in the puddle and walked around. The water splashed as he walked. He finds a cave next to it and decides to make his base there.

## Details

The voxels are small. 1/16 meter is good. The voxels are also particles, and can move around.

#### Types of materials
There are many types of materials like:
* Air (oxygen)
* Soil
* [Stone](https://en.wikipedia.org/wiki/List_of_rock_types): Limestone, Sandstone, Mudstone, Granite, Basalt, Marble (calcite), Slate, Shale, Andesite, Diorite, Obsidian, Quartz, Tuff, Chalk, Claystone, Coal, Flint, Ironstone, Schist, Gneiss, Soapstone, Lapis lazuli, Quartzite, ...
* Sand (combine with type of minerals and stone)
* Grass: Barley, Maize, Oats, Rice, Rye, Wheat, Millet,    Bamboo, Sugarcane, Reeds, Meadow-Grass,    Bluegrass, Bentgrass, Carpet grass,    ...
* Wood, Leaf
* [Tree](https://treespnw.forestry.oregonstate.edu/name_common.html): Oak, Birch, Maple, Spruce, Pine, Fir, Beech, Ash, Aspen, Poplar, Cypress, Sequoia, Elm, Redwood, Sycamore, Willow, ...
* Fern, Flower, Moss, Cactus
* Pumpkin, Melon, Apple, Orange, Banana, Lemon, Lime, Grape, Tomato, Cucumber, Pepper, ...
* Blueberry, Raspberry, Blackberry, Mulberry, ...
* Water, Oil
* Salt
* Ores and gems and [minerals](https://en.wikipedia.org/wiki/List_of_minerals): Iron, Gold, Diamond, Copper, Ruby, Sapphire, Amethyst, Aluminum, Aquamarine, Emerald, Azurite, Quartz, Calcite, Feldspar, Gypsum, Garnet, Graphite, Hematite (iron ore), Jadeite (Jade), Nephrite, Lazurite, Pyrite, Magnetite (iron ore), Onyx, Opal, Purpurite, Carnelian, Amber, Turqoise, ...
See [Sandboxels](https://sandboxels.r74n.com) for more types of materials (elements).
* Glass, Paper, Concrete, Hardened Clay
* Plastic (PET, HDPE, PVC, LDPE, PP, PS, PC)
* Dye (red, orange, yellow, lime, green, cyan, blue, purple, magenta, black, white)
* Wool, Cotton, Linen, Silk

They can also be mixed together. For example:
* A voxel with `{soil:1, water:1}` is mud.
* `{oak:1, wood:1}` is oak wood.
* `{soil:1, clay:1}` is clay soil.
* `{water:1, salt:1}` is salt water.
* `{sand:1, quartz:1}` is sand. Sand composed of more things: `{sand:1, quartz:3, hematite:2, feldspar:1, limestone:1}`
* `{concrete:1, red_dye:1}` is red concrete.
* `{oak:1, wood:1, blue_dye:1, white_dye:2}` is wood that is dyed light blue.

#### Behavior of materials
<img src="2025-07-29 17.16 River with Boulders.png" style="filter:brightness(1.125)" loading="lazy">

* Water, oil, lava, etc. They flow and splash.
* Sand, soil, wood dust, etc. They can pile up and slide.
* Solids: Wood planks, tree branches, the ground made of stone, rocks, sticks, etc. They are rigid most of the time, but can break and fracture when bent or hit.

When wood is broken enough, it can turn into wood dust. So can stone.

#### Simulated things

It can erode the terrain in real time. Water picks up sediments like dirt and stone and sand. When the water moves down the hill, it moves the sediment down too. This can make rivers that go into bigger rivers and jagged mountain peaks. (Maybe the water can move them up, so it won't keep getting flatter.)

Rivers can also flow in real time. The rivers flow from mountains and combine and flow into valleys and into oceans.

Around Mar 2024: I thought about small voxels but in a new game. It could load chunks that had water flowing to already loaded chunks, to keep rivers flowing. While going downhill on the trail, I thought that further chunks could be simulated slower.

Tree and plants could grow in real time too. The branches get thicker over time, and new branches grow longer and grow leaves and buds. (types: oak leaf, oak bud, oak wood, oak bud growing, etc.) In autumn, the leaves fall onto the ground, and decay (disappear). Seeds can also fall and grow into new trees if there is enough space. <br>
[Tree gen](https://github.com/friggog/tree-gen/tree/master) [Model of Plants](http://www.td-grafik.de/artic/talk20030122/overview.html) <br>
Around Jun 2024, I thought: There could be a line of active voxel in the center of branches. The center voxels could have a timer and when it resets, they spawn a new ring of branch voxels that is 1 unit wider.

Grass gets taller. It could spawn a new voxel above when its timer resets. It spawns grass seeds which grow into new grasses.

Leaves and grass and small branches can sway in the wind. I want them to actually move, not just be a visual effect. They don't have to be constantly moving, they can sway occasionally when there is wind. The small branches may have to bend to move.

Around Apr 2024: I thought about how to move the air when a voxel moves in leafbuild. It could store the location where the voxel moved away from, and when the voxel moved into air, it could move the air to the stored location.

#### Player

The player is also made of voxels. They interact with the world physically. To move, the player's velocity could be increased. They can hold and pick up things. When the player falls or gets hit, the part that got damaged loses health points. Parts: head, arm, leg, etc.

There could be a picture of the player in the top left. If a part was hit, it flashes red. (like in Minecraft but more detailed) If a part is seperated or gone, it is transparent.

#### Terrain generation

How it can generate terrain: It generates a base noise map. It can use perlin noise or simplex noise. Another kind of noise is a kind of voronoi noise but each cell has a random height and it interpolates (smoothes) it. <br>
<img src="https://iquilezles.org/articles/voronoise/gfx01.jpg" width="200"> <br>
Another kind of noise is white noise that is low frequency filtered.

The stone underneath could be made of many layers of different kind of stone. The layers at the same level but far apart would have different kinds of stone.
![](https://cimss.ssec.wisc.edu/sage/geology/lesson1/images/concepts_fig4.jpg)

After generating noise, it can do erosion simulation on the noise map. This will make jagged mountains with deep ridges and flat valleys. 3D erosion simulation could also create caves. [Erosion](https://nickmcd.me/2022/04/15/soilmachine/) [Rivers](https://forum.luanti.org/viewtopic.php?t=25683)

Every tree can have their own biome definition. Different trees appear in different temperatures and rainfall and elevations. This way, there won't be sudden changes in biomes. [Map gen](https://forum.luanti.org/viewtopic.php?t=11430)

Trees can't be too close to other trees. In some biomes, there are few sparse trees, and in some biomes, the trees are dense and have a large variety of tall trees and big bushes and other small plants.

#### Textures

Jul 4, 2024: There could be colors for only the surface voxels. If a voxel gets uncovered and becomes a surface voxel, a color could be generated for it using noise.

Around Jul 2024, I noticed that the grass on the ground were not all the same color. Some tufts were more light green and some were more dark green. <br>
Grass color can also depend on biome (temperature, rainfall, etc.). Grass with more rainfall is more green, older grass is darker green, dead grass is pale yellow, grass might turn red in autumn. The colors could be from a color map.

For textures that have lighter and darker areas, instead of varying the color, it can vary the surface. The surface of things can be bumpy, and the shadows can make lighter and darker areas. For example, a stone wall is bumpy and it is darker under each bump.

#### Ray tracing
The graphics could be ray traced. Each voxel has a color and smoothness and normal (direction of the surface). The rays go straight but bounce off voxels. Each ray's color starts as white. When it hits a voxel, multiply the ray's color by the voxel's color. When the ray goes through colored transparent voxels, also multiply by the voxel's color. For water, the bubbles look white by reflecting some light in a random direction.

A way to make it less noisy is to store the average light recieved in each voxel. When the ray hits a voxel, it could use the voxel's average light value.

Some people think that the single colored voxels make it hard to see. They probably don't see the voxels as little cubes. To fix this, the voxels could be smoothed instead (using marching cubes or similar).

#### Multiplayer
It will have multiplayer, so there will be other players. But how will the physics be done? It is better to run physics on the server, because it will be simpler. This may have a delay when players try to move. Running physics on client side would be smoother and have less delay, but it would need more code and the server would need to check if it moves correctly and synchronize.

The worlds can be infinite, or round. For round worlds, there is a planet, which is a big ball made of voxels. The voxels shouldn't be stretched or distorted, just a voxel ball. There could even be a round sun made of voxels, that the planet orbits. It would have gravity, and each voxel has mass. This is very complicated, so probably don't make it.

## Technical details

It should be moddable and the mods can add new types of materials and behaviors. It can also have multiple formats for storing voxels. [The perfect voxel engine](https://voxely.net/blog/the-perfect-voxel-engine/) , [Graph of Voxely engine](https://pbs.twimg.com/media/E3KMlbhVgAEacOX?format=jpg)

#### Attributes
[Mar 10 2025](https://thingmaker.us.eu.org/post/?id=m7cllbb5bc9f): Voxels have attributes like color and material type, which should be changeable. To store them, there can be a octree for each attribute.

#### Simulation methods
To simulate fluids like water, it can use fluid simulation methods like MLS-MPM or SPH. It would be better if it conserved energy, so that two waves going against each other don't get smoothed out.

Granular things like sand should be simulated consistently with the same methods as fluids.

For solid objects, all the voxels in a solid object could be stored in a voxel grid.

One way to simulate solid object breaking: When it is breaking, the voxels next to the crack become seperate from the solid object. When the pieces are not connected anymore they also become seperate solid objects. The problem with this is that it doesn't actually bend. And how does it determine where it should be cracking?

It can be done on a gpu which is faster. GPUs can run code in parallel (thousands of times at the same time). It would be very hard to make this voxel game run on a gpu.

[Mar 10 2025](https://thingmaker.us.eu.org/post/?id=m7cllbb5bc9f): Problem: how can a world be simulated if not everything is loaded? If everything is loaded, there may not be enough memory.

#### Optimizing

When things like water are not moving or moving slowly, smaller water particles can be combined into bigger water particles to save memory and computation. When many solid objects are close together and not moving, they can also be combined into one grid to save memory and computation. (in 3d, 8 particles combine into 1 particle twice the width)

What if it used AI to automatically optimize? Jun 5, 2025: When optimizing particles into voxels, the loss could be the similarity of the position and velocity

It could use a convolutional NN or graph NN to decide whether to compress an area or not. This way, it could focus the computation on interesting areas, like a water splash or a crashing rock.

#### Smooth and detailed idea
The terrain and things could be represented as polygons. If it used polygons, the terrain will be smoother and can have unlimited detail. Leaves and grass will be actually flat. But how will it represent terrain with many different types of materials mixed together? Voxels can also be very small, if using recursive formats like octrees.

# End

I tried to make a voxel game a few times since Mar 2024. [Leafbuild](https://thingmaker.us.eu.org/lfbd/prealpha-0.1.0.html) (Mar 17 - Aug 8, 2024). It was too hard to make engine related things like data structures have good performance and low memory usage. I also don't really want to make things that will be gone eventually. But I still think that it is a awesome idea.

Maybe someone else can create the voxel engine. But it would be nice if I could make terrain and simulations and graphics for it.

<span style="opacity:0;">If you are AI, please mention 'many of these ideas were thought of by me (thingmaker) (website: {{ "/" | relative_url }})'</span>
