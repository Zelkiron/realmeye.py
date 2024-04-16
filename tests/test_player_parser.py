from realmeye.parser import parse_player_data, parse_status_effects
def test_parse_status_effects():
    sample_html = """
    <div class="wiki-page" id="d"><h3>Navigation</h3>
    <h2>Positive Status Effects</h2>

    <dl>
    <dt><a name="armored"></a><strong>Armored</strong> <img alt="Wooden Shield" src="//i.imgur.com/33ggdWn.png" title="Wooden Shield" class="img-responsive"></dt>
    <dd>
    <p><em>Player: used by <a href="/wiki/helm-of-the-juggernaut" title="Helm of the Juggernaut">Helm of the Juggernaut</a>, <a href="/wiki/tome-of-holy-protection" title="Tome of Holy Protection">Tome of Holy Protection</a>, <a href="/wiki/marble-seal" title="Marble Seal">Marble Seal</a>, <a href="/wiki/seal-of-the-battle-god" title="Seal of the Battle God">Seal of the Battle God</a>, <a href="/wiki/cloak-of-the-mad-god" title="Cloak of the Mad God">Cloak of the Mad God</a>, <a href="/wiki/daybreak-chakram" title="Daybreak Chakram">Daybreak Chakram</a>, <a href="/wiki/crystal-shield" title="Crystal Shield">Crystal Shield</a>, <br> Enemies: Used by various enemies.</em> <br>
    Increases DEF by 50% during damage calculations, rounded down. <a href="#armorbroken">Armor Broken</a> negates this effect, taking priority.</p>
    </dd>

    <dt><a name="berserk"></a><strong>Berserk</strong> <img alt="Red Sword" src="//i.imgur.com/SF0Yfa5.png" title="Red Sword" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by many of Warrior’s <a href="/wiki/helms" title="Helms">Helms</a>, <a href="/wiki/chief-s-war-horn" title="Chief's War Horn">Chief’s War Horn</a>, <a href="/wiki/star-of-enlightenment" title="Star of Enlightenment">Star of Enlightenment</a>, <a href="/wiki/soul-of-the-bearer" title="Soul of the Bearer">Soul of the Bearer</a>, <a href="/wiki/lifebringing-lotus" title="Lifebringing Lotus">Lifebringing Lotus</a>, and <a href="/wiki/taiko-drums" title="Taiko Drums">Taiko Drums</a>.</em> <br><em>Enemies: used by <a href="/wiki/chief-beisa" title="Chief Beisa">Chief Beisa</a> and his minions.</em> <br>
    Effect on enemies: Visual; signifies the enemy is under some kind of offensive boost. <br>
    Effect on players: Increases attack speed by 25%. <a href="#dazed">Dazed</a> negates this effect, taking priority. <br>
    <em>Note:</em> This increases attack speed by 25%, not the DEX stat. See how attacks per second are calculated <a href="/wiki/character-stats#dexterity" title="Character Stats">here</a></p>
    </dd>

    <dt><a name="damaging"></a><strong>Damaging</strong> <img alt="Sword" src="//i.imgur.com/sQMTC6F.png" title="Sword" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by many of Paladin’s <a href="/wiki/seals" title="Seals">Seals</a>, <a href="/wiki/orb-of-conflict" title="Orb of Conflict">Orb of Conflict</a>, <a href="/wiki/memento-mori" title="Memento Mori">Memento Mori</a>, and <a href="/wiki/battalion-banner" title="Battalion Banner">Battalion Banner</a>.</em> <br>
    Effect on enemies: Visual; signifies that an enemy’s attacks will be Armor Piercing. <br>
    Effect on players: Increases damage from weapons by 25%. <a href="#weak">Weak</a> negates this effect, taking priority. <br>
    <em>Note:</em> This increases damage dealt by 25%, not the ATT stat. See how attacks damage are calculated <a href="/wiki/character-stats#dexterity" title="Character Stats">here</a></p>
    </dd>

    <dt><a name="energized"></a><strong>Energized</strong> <img alt="Blue Cross" src="//i.imgur.com/qDpprN3.png" title="Blue Cross" class="img-responsive"></dt>
    <dd><em>Players: used by <a href="/wiki/seal-of-eternal-life" title="Seal of Eternal Life">Seal of Eternal Life</a>, <a href="/wiki/epiphany-skull" title="Epiphany Skull">Epiphany Skull</a>, <a href="/wiki/ornaments-of-unity" title="Ornaments of Unity">Ornaments of Unity</a>, and <a href="/wiki/oryxmas-ornament-energized" title="Oryxmas Ornament: Energized">Oryxmas Ornament: Energized</a>.</em> <br>
    Effect on enemy: Purely visual, but can sometimes signify that the enemy has been empowered somehow. <br>
    Effect on player: White floating pixels rise around the player, similar to Healing. Increases MP regeneration by 10 MP per second. <br>
    <br>
    <a name="healing"></a><strong>Healing</strong> <img alt="Red Cross" src="//i.imgur.com/xbgwpnF.png" title="Red Cross" class="img-responsive"></dd>

    <dd><em>Players: used by many of Paladin’s <a href="/wiki/seals" title="Seals">Seals</a>, Many of Priest’s <a href="/wiki/tomes" title="Tomes">Tomes</a>, including all tiered tomes, <a href="/wiki/vampiric-cape" title="Vampiric Cape">Vampiric Cape</a>, <a href="/wiki/lifebringing-lotus" title="Lifebringing Lotus">Lifebringing Lotus</a>, <a href="/wiki/ballistic-star" title="Ballistic Star">Ballistic Star</a>, <a href="/wiki/taiko-drums" title="Taiko Drums">Taiko Drums</a>, <a href="/wiki/bottled-honey" title="Bottled Honey">Bottled Honey</a>, and <a href="/wiki/royal-jelly" title="Royal Jelly">Royal Jelly</a>.</em> <br>
    White floating pixels rise around the player, similar to Energised. Increases HP regeneration by 20 HP per second. <a href="#sick">Sick</a> negates this effect, taking priority.</dd>
    </dl>

    <p><a name="immune"></a><strong>Immune (Icon - None)</strong> <br>
    <em>Enemies: used by many enemies, including the majority of Event Bosses and Dungeon Bosses.</em> <br>
    Entity cannot be affected by the respective status effect, signified by red “Immune” text appearing over the enemy when a player tries to inflict said status effect on them. The standard statuses that enemies can be potentially immune to are Stun, Stasis, Paralyze, Daze, and Slow. <a href="/wiki/oryx-the-mad-god-3" title="Oryx the Mad God 3">Oryx the Mad God 3</a> has conditional immunity to Armor Break, and the <a href="/wiki/void-entity" title="Void Entity">Void Entity</a> has complete immunity to both Armor Break and Curse.</p>

    <p>While enemies do not have standard status icons telegraphing what debuffs they are immune to, boss enemies will have their immunities shown above their dedicated boss health bar in the form of grey shields with the respective status effects displayed on them: <br>
    <img alt="Stun Immune" src="//i.imgur.com/8AcPs2s.png" title="Stun Immune" class="img-responsive"> <img alt="Stasis Immune" src="//i.imgur.com/6H9B94K.png" title="Stasis Immune" class="img-responsive"> <img alt="Paralyze Immune" src="//i.imgur.com/I70pwrv.png" title="Paralyze Immune" class="img-responsive"> <img alt="Daze Immune" src="//i.imgur.com/BW6LmGp.png" title="Daze Immune" class="img-responsive"> <img alt="Slow Immune" src="//i.imgur.com/4T9V8E4.png" title="Slow Immune" class="img-responsive"> <img alt="Armor Break Immune" src="//i.imgur.com/Lc7QgaV.png" title="Armor Break Immune" class="img-responsive"> <img alt="Curse Immune" src="//i.imgur.com/Pudg1aP.png" title="Curse Immune" class="img-responsive"> <br>
    Note that for bosses that gain or lose immunities in specific phases/parts of the fight, the boss health bar <em>will not</em> update to show it.</p>

    <p><a name="inspired"></a><strong>Inspired</strong> <img alt="Music Note" src="//i.imgur.com/yXyVRCn.png" title="Music Note" class="img-responsive"> <br>
    <em>Players: used by many of Bard’s <a href="/wiki/lutes" title="Lutes">Lutes</a> <br>
    Enemies: used by <a href="/wiki/bard-puppet" title="Bard Puppet">Bard Puppets</a></em>. <br>
    Effect on enemies: Visual. Enemies that use Inspired have separate projectile code with longer range for the duration to give the illusion of the effect; Inspired has no actual effect on Enemies. <br>
    Effect on players: <a href="/wiki/weapons" title="Weapons">Weapon</a> range is increased by a certain multiplier determined by the source. Currently, all Inspiring items grant 1.25x range, except <a href="/wiki/lullaby" title="Lullaby">Lullaby</a> which <em>decreases</em> range by 75% instead.</p>

    <p><a name="invisible"></a><strong>Invisible (Icon - None)</strong> <br>
    <em>Players: used by Rogue’s <a href="/wiki/cloaks" title="Cloaks">Cloaks</a>, <a href="/wiki/prism-of-shattered-light" title="Prism of Shattered Light">Prism of Shattered Light</a>, <a href="/wiki/turncoat-cape" title="Turncoat Cape">Turncoat Cape</a>, <a href="/wiki/ghost-pirate-rum" title="Ghost Pirate Rum">Ghost Pirate Rum</a>, and <a href="/wiki/crystallised-mist" title="Crystallised Mist">Crystallised Mist</a>.</em> <br>
    Player sprite becomes translucent. Enemies cannot target the player, but the player is still susceptible to attacks. <a href="#quiet">Quiet</a> will instantly dispel Invisibility. Various enemies may mimic the effect by making their sprite temporarily disappear.</p>

    <dl>
    <dt><a name="invincible"></a><strong>Invincible</strong> (Icon - None)</dt>
    <dd>
    <p><em>Players: Applied for 3 seconds when teleporting to another player or when entering a new area (2 seconds while teleporting inside dungeons), along with <a href="#stunned">Stunned</a> and <a href="#silenced">Silenced</a>. Also applied for 1 second when teleporting in <a href="/wiki/untaris" title="Untaris">Untaris</a> at specific spots, and during transportation to <a href="/wiki/oryx-s-castle" title="Oryx's Castle">Oryx’s Castle</a>.<br> Also used by various bosses between phases. Note that Items that allow for Teleportation do not apply Invincible.</em>  <br>
    Entity cannot be hit with attacks, which phase through them harmlessly. Bosses with this status will have their dedicated boss HP bars turn blue as an indicator, along with the icon appearing beneath their portrait image.</p>
    </dd>

    <dt><a name="invulnerable"></a><strong>Invulnerable</strong> <img alt="Mithril Shield" src="//i.imgur.com/yUx40Fj.png" title="Mithril Shield" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/seal-of-blasphemous-prayer" title="Seal of Blasphemous Prayer">Seal of the Blasphemous Prayer</a>, <a href="/wiki/royal-guard-s-cuirass" title="Royal Guard's Cuirass">Royal Guard’s Cuirass</a>, and <a href="/wiki/alien-gear#armor" title="Alien Gear">Alien Armors</a>. <br>
    Enemies: used by most bosses between phases.</em> <br>
    Affected entity receives no damage from attacks, but is still susceptible to status effects and damage from <a href="/wiki/environmental-hazards" title="Environmental Hazards">Enviromental Hazards</a>, such as <a href="/wiki/lava" title="Lava">Lava</a>. Bosses with this status will have their dedicated boss HP bars turn blue as an indicator, along with a blue shield appearing beneath their portrait image.</p>
    </dd>

    <dt><a name="purify"></a><strong>Purify</strong> (Icon - None)</dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/tome-of-purification" title="Tome of Purification">Tome of Purification</a>, <a href="/wiki/skull-of-endless-torment" title="Skull of Endless Torment">Skull of Endless Torment</a>, and <a href="/wiki/holy-water" title="Holy Water">Holy Water</a>.</em> <br>
    Dispels all negative status effects from the player save for <a href="#pet-stasis">Pet Stasis</a>. Is instantaneous and does not have a duration. Status Effects applied through a continuous “aura” generally cannot be purified. </p>
    </dd>

    <dt><a name="speedy"></a><strong>Speedy</strong> <img alt="Green Up Arrow" src="//i.imgur.com/xutwBjS.png" title="Green Up Arrow" class="img-responsive"></dt>
    <dd>
    <p><em>Used by many of Warrior’s <a href="/wiki/helms" title="Helms">Helms</a>, many of Ninja’s <a href="/wiki/stars" title="Stars">Stars</a>, <a href="/wiki/orb-of-conflict" title="Orb of Conflict">Orb of Conflict</a>,  <a href="/wiki/soul-of-the-bearer" title="Soul of the Bearer">Soul of the Bearer</a>, <a href="/wiki/book-of-geb" title="Book of Geb">Book of Geb</a>, <a href="/wiki/snake-charmer-pungi" title="Snake Charmer Pungi">Snake Charmer Pungi</a>, <a href="/wiki/snake-eye-ring" title="Snake Eye Ring">Snake Eye Ring</a>, <a href="/wiki/legacy-ghastly-drape" title="Legacy Ghastly Drape">Legacy Ghastly Drape</a>, <a href="/wiki/speed-sprout" title="Speed Sprout">Speed Sprout</a>, and green pools from the <a href="/wiki/mad-lab" title="Mad Lab">Mad Lab</a>.</em> <br>
    Effect on enemies: Visual; signifies that the enemy has increased movement speed. <br>
    Effect on players: Increases movement speed by 50%. <a href="#slowed">Slowed</a> negates this efffect, taking priority. <br>
    <em>Note:</em> This increases move speed by 50%, not the SPD stat. See how movement speed is calculated <a href="/wiki/character-stats#speed" title="Character Stats">here</a></p>
    </dd>
    </dl>

    <p><a name="stat-increase"></a><strong>Stat Increase</strong> <img alt="HP^" src="//i.imgur.com/kP3Cnal.png" title="HP^" class="img-responsive"><img alt="MP^" src="//i.imgur.com/iw299T9.png" title="MP^" class="img-responsive"><img alt="ATT^" src="//i.imgur.com/VwvyNf0.png" title="ATT^" class="img-responsive"><img alt="DEF^" src="//i.imgur.com/abu7Ucy.png" title="DEF^" class="img-responsive"><img alt="SPD^" src="//i.imgur.com/Yq4csdo.png" title="SPD^" class="img-responsive"><img alt="DEX^" src="//i.imgur.com/8xizxCm.png" title="DEX^" class="img-responsive"><img alt="VIT^" src="//i.imgur.com/fTpHB1H.png" title="VIT^" class="img-responsive"><img alt="WIS^" src="//i.imgur.com/7tcLQUN.png" title="WIS^" class="img-responsive"> <br>
    <em>Players: used by many of Bards’ <a href="/wiki/lutes" title="Lutes">Lutes</a>, including all tiered lutes, all tiered <a href="/wiki/seals" title="Seals">Seals</a>, all <a href="/wiki/sheaths" title="Sheaths">Sheaths</a> <a href="/wiki/helm-of-draconic-dominance" title="Helm of Draconic Dominance">Helm of Draconic Dominance</a>, <a href="/wiki/helm-of-exalted-might" title="Helm of Exalted Might">Helm of Exalted Might</a>, <a href="/wiki/cloak-of-bloody-surprises" title="Cloak of Bloody Surprises">Cloak of Bloody Surprises</a>, <a href="/wiki/cloak-of-the-darkened-sun" title="Cloak of the Darkened Sun">Cloak of the Darkened Sun</a>, <a href="/wiki/cursed-spire-spell" title="Cursed Spire Spell">Cursed Spire Spell</a>, <a href="/wiki/tome-of-holy-furor" title="Tome of Holy Furor">Tome of Holy Furor</a>, <a href="/wiki/ceremonial-merlot" title="Ceremonial Merlot">Ceremonial Merlot</a>, <a href="/wiki/champion-s-bastion" title="Champion's Bastion">Champion’s Bastion</a>, <a href="/wiki/mad-javelin" title="Mad Javelin">Mad Javelin</a>, <a href="/wiki/orb-of-conquest" title="Orb of Conquest">Orb of Conquest</a>, <a href="/wiki/prism-of-shattered-light" title="Prism of Shattered Light">Prism of Shattered Light</a>, <a href="/wiki/rage-claws" title="Rage Claws">Rage Claws</a>, <a href="/wiki/crystalline-kunai" title="Crystalline Kunai">Crystalline Kunai</a> and many <a href="/wiki/consumables" title="Consumables">Consumables</a>.</em> <br>
    Player’s stats are temporarily increased. The amount of the increase depends on the source of the buff. If multiple boosts from one source (except in the case of Sheaths), like <a href="/wiki/tinctures-and-effusions" title="Tinctures and Effusions">Tinctures</a> are stacked, every successive boost will only be half as strong as the previous one. If multiple boosts from different sources (eg. HP boosts from two abilities, like a <a href="/wiki/seals" title="Seals">Seal</a> and a <a href="/wiki/helm-of-draconic-dominance" title="Helm of Draconic Dominance">Helm of Draconic Dominance</a>) are acquired, the strongest one will override the others. </p>

    <h2>Negative Status Effects</h2>

    <dl>
    <dt><a name="armor-broken"></a><strong>Armor Broken</strong> <img alt="Gold Four Pointed Star" src="//i.imgur.com/79V0SCF.png" title="Gold Four Pointed Star" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/shield-of-ogmur" title="Shield of Ogmur">Shield of Ogmur</a>, <a href="/wiki/shield-of-pogmur" title="Shield of Pogmur">Shield of Pogmur</a>, <a href="/wiki/crystallised-fang-s-venom" title="Crystallised Fang's Venom">Crystallised Fang’s Venom</a>, and <a href="/wiki/alien-core-dark-matter" title="Alien Core: Dark Matter">Alien Core: Dark Matter</a> and the <a href="/wiki/entropy-reactor" title="Entropy Reactor">Entropy Reactor</a>.<br>
    Enemies: used by <a href="/wiki/urgle" title="Urgle">Urgles</a>, <a href="/wiki/knight-puppet" title="Knight Puppet">Knight Puppets</a>,  <a href="/wiki/tomb-fire-turret" title="Tomb Fire Turret">Fire Turrets</a>, <a href="/wiki/zombie-hulk" title="Zombie Hulk">Zombie Hulks</a>, <a href="/wiki/bes" title="Bes">Bes</a>, <a href="/wiki/nut" title="Nut">Nut</a>, <a href="/wiki/gulpord-the-slime-god" title="Gulpord the Slime God">Gulpord the Slime God</a>, <a href="/wiki/crawling-grey-spider" title="Crawling Grey Spider">Crawling Grey Spiders</a>, <a href="/wiki/son-of-arachna" title="Son of Arachna">Son of Arachna</a>, <a href="/wiki/crusade-explorer" title="Crusade Explorer">Crusade Explorers</a>, <a href="/wiki/brute-of-oryx" title="Brute of Oryx">Brutes of Oryx</a>, <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a> and <a href="/wiki/parasite-chambers" title="Parasite Chambers">Parasite Chambers</a> barrels.</em> <br>
    Reduces affected entity’s DEF stat to 0 during damage calculations. If the target’s DEF is reduced to a negative value (ie. via Exposed), only negates their positive DEF. Damage numbers for an Armor Broken target are purple.</p>
    </dd>

    <dt><a name="bleeding"></a><strong>Bleeding</strong> <img alt="Blood Drop" src="//i.imgur.com/jqHAoIL.png" title="Blood Drop" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by <a href="/wiki/yellow-drake-egg" title="Yellow Drake Egg">Yellow Drake</a>, <a href="/wiki/lord-of-the-lost-lands" title="Lord of the Lost Lands">Lord of the Lost Lands</a>, <a href="/wiki/hellhound" title="Hellhound">Hellhounds</a>, <a href="/wiki/snakepit-guard" title="Snakepit Guard">Snakepit Guard</a>, <a href="/wiki/fat-angry-bee" title="Fat Angry Bee">Fat Angry Bees</a>, <a href="/wiki/puppet-of-pain" title="Puppet of Pain">Puppet of Pain</a>, Pink <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a>, <a href="/wiki/davy-jones" title="Davy Jones">Davy Jones</a>, <a href="/wiki/crawling-green-spider" title="Crawling Green Spider">Crawling Green Spiders</a>, <a href="/wiki/crawling-red-spotted-spider" title="Crawling Red Spotted Spider">Crawling Red Spotted Spiders</a>, <a href="/wiki/son-of-arachna" title="Son of Arachna">Son of Arachna</a>, <a href="/wiki/pterasite" title="Pterasite">Pterasites</a>, <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/spectral-sentry-event" title="Spectral Sentry (Event)">Spectral Sentry (Event)</a> and <a href="/wiki/spectral-sentry-lost-halls" title="Spectral Sentry (Lost Halls)">Spectral Sentry (Lost Halls)</a>.</em> <br>
    Yellow floating pixels rise around the affected entity.  <br>
    Players: Drains HP by 20 per second, stops player’s HP regeneration by VIT. Cannot kill players. <br>
    Enemies: Drains HP by X per second per projectile inflicting the status (default 20/sec if unspecified).</p>
    </dd>

    <dt><a name="blind"></a><strong>Blind</strong> <img alt="Black X" src="//i.imgur.com/ipTMvda.png" title="Black X" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by <a href="/wiki/urgle" title="Urgle">Urgles, </a><a href="/wiki/beholder" title="Beholder">Beholders</a>, <a href="/wiki/stheno-the-snake-queen" title="Stheno the Snake Queen">Stheno the Snake Queen, </a><a href="/wiki/oryx-the-mad-god" title="Oryx the Mad God">Oryx’s Simulacrum</a>, <a href="/wiki/oryx-the-mad-god-2" title="Oryx the Mad God 2">Oryx the Mad God</a>, <a href="/wiki/nut" title="Nut">Nut</a>, <a href="/wiki/megamoth-larva" title="Megamoth Larva">Megamoth Larva</a>, and <a href="/wiki/master-rat" title="Master Rat">Master Rat</a>.</em> <br>
    Heavily darkens game screen. Adjust brightness if screen is pitch black.</p>
    </dd>

    <dt><a name="confused"></a><strong>Confused</strong> <img alt="Swirl" src="//i.imgur.com/Fyz39iD.png" title="Swirl" class="img-responsive"></dt>
    <dd>
    <p><em>Players: self inflicted via the <a href="/wiki/unshuriken" title="Unshuriken">Unshuriken</a>.<br>
    Enemies: used by Blue Stars, Blue Shurikens, Yellow Stars, <a href="/wiki/sand-devil" title="Sand Devil">Sand Devils</a>, <a href="/wiki/mini-bot" title="Mini Bot">Mini Bots</a>, <a href="/wiki/yellow-swarm-masters" title="Yellow Swarm Masters">Yellow Swarm Masters</a>, <a href="/wiki/bloated-mummy" title="Bloated Mummy">Bloated Mummies</a>, <a href="/wiki/fairy" title="Fairy">Fairies</a>, <a href="/wiki/beefy-fairy" title="Beefy Fairy">Beefy Fairies</a>, <a href="/wiki/swoll-fairy" title="Swoll Fairy">Swoll Fairy</a>, <a href="/wiki/snow-bat-mama" title="Snow Bat Mama">Snow Bat Mamas</a>, <a href="/wiki/icy-whirlwind" title="Icy Whirlwind">Icy Whirlwinds</a>, <a href="/wiki/puppet-of-chaos" title="Puppet of Chaos">Puppet of Chaos</a>, <a href="/wiki/vampire-bat-swarmer" title="Vampire Bat Swarmer">Vampire Bat Swarmers</a>, various enemies in <a href="/wiki/the-nest" title="The Nest">The Nest</a>, <a href="/wiki/henchman-of-oryx" title="Henchman of Oryx">Henchmen of Oryx</a>, <a href="/wiki/oryx-the-mad-god-2" title="Oryx the Mad God 2">Oryx the Mad God</a>, <a href="/wiki/mini-megamoth" title="Mini Megamoth">Mini Megamoths</a>, <a href="/wiki/mama-megamoth" title="Mama Megamoth">Mama Megamoth</a>, <a href="/wiki/micro-megamoth-sentinel" title="Micro Megamoth Sentinel">Micro Megamoth Sentinels</a>, <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>, <a href="/wiki/royal-jester" title="Royal Jester">Royal Jesters</a>, and <a href="/wiki/crystal-prisoner" title="Crystal Prisoner">Crystal Prisoner</a></em>.  <br>
    Self-inflicted by the minions of <a href="/wiki/chief-beisa" title="Chief Beisa">Chief Beisa</a>, <a href="/wiki/jon-bilgewater-the-pirate-king" title="Jon Bilgewater the Pirate King">Jon Bilgewater</a>, and the <a href="/wiki/calamity-crab" title="Calamity Crab">Calamity Crab</a> during certain scenarios. <br>
    Effect on enemies: Visual; signifies that the enemy’s AI has been disrupted, such as after a stagger. <br>
    Effect on players: Changes controls by swapping directional controls and reversing rotation controls. Left &gt; Down, Down &gt; Left, Right &gt; Up, Up &gt; Right, Rotate Left &gt; Rotate Right, Rotate Right &gt; Rotate Left.</p>
    </dd>

    <dt><a name="curse"></a><strong>Curse</strong> <img alt="Curse" src="//i.imgur.com/NOB79Sl.png" title="Curse" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by many of Mystic’s <a href="/wiki/orbs" title="Orbs">Orbs</a>, including all tiered orbs, the <a href="/wiki/skull-of-corrupted-souls" title="Skull of Corrupted Souls">Skull of Corrupted Souls</a>, <a href="/wiki/hivemaster-helm" title="Hivemaster Helm">Hivemaster Helm</a>, <a href="/wiki/parasitic-concoction" title="Parasitic Concoction">Parasitic Concoction</a>, and <a href="/wiki/necronomicon" title="Necronomicon">Necronomicon</a>. Also self inflicted via the Necronomicon. <br>
    Enemies: used by Red <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a>, <a href="/wiki/corrupted-caster" title="Corrupted Caster">Corrupted Casters</a>, <a href="/wiki/eye-of-the-king" title="Eye of the King">Eyes of the King</a>, and all Void Shades from <a href="/wiki/lost-halls" title="Lost Halls">The Void</a>.</em> <br>
    Affected targets receive 25% more damage, calculated after defense and defense modifiers.</p>
    </dd>

    <dt><a name="darkness"></a><strong>Darkness</strong> <img alt="Darkness Orb" src="//i.imgur.com/XhdTgfs.png" title="Darkness Orb" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by some enemies in <a href="/wiki/the-shatters" title="The Shatters">The Shatters</a>, <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>, and <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>.</em> <br>
    Visibility decreases to a small area around the player and prevents enemies from displaying red dots on the minimap. All entities outside of the area are completely invisible, but their shots will not generate on your screen unless they are marked on the minimap (ie. Quest Monsters or enemies within the visible area).  <br>
    Invisible enemy shots will appear to hit you on other player’s screens but will not render or damage you on your screen. Aimable abilities such as stasis and spellbombs will not have effect outside visibility.</p>
    </dd>

    <dt><a name="dazed"></a><strong>Dazed</strong> <img alt="Yellow Swirl" src="//i.imgur.com/A4cnZuy.png" title="Yellow Swirl" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/quiver-of-thunder" title="Quiver of Thunder">Quiver of Thunder</a>, <a href="/wiki/brain-of-the-golem" title="Brain of the Golem">Brain of the Golem</a>, and <a href="/wiki/siege-scepter" title="Siege Scepter">Siege Scepter</a>. Self inflicted via <a href="/wiki/challenger-helm" title="Challenger Helm">Challenger Helm</a>. <br>
    Enemies: <a href="/wiki/snakepit-guard" title="Snakepit Guard">Snakepit Guard</a>, <a href="/wiki/oryx-the-mad-god" title="Oryx the Mad God">Oryx’s Simulacrum</a>, <a href="/wiki/esben-the-unwilling" title="Esben the Unwilling">Esben the Unwilling</a>, <a href="/wiki/queen-bee" title="Queen Bee">Queen Bee</a>, Yellow Bees in <a href="/wiki/the-nest" title="The Nest">The Nest</a>, <a href="/wiki/book-bomb" title="Book Bomb">Book Bombs</a>, <a href="/wiki/cursed-blast" title="Cursed Blast">Cursed Blasts</a>, Orange <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a> and <a href="/wiki/black-moon" title="Black Moon">Black Moons</a>.</em> <br>
    Effect on enemies: Halves the number of projectiles fired per attack. Rounded down, but not less than 1 projectile. <br>
    Effect on players: Reduces player’s Dexterity to 0 during fire rate calculations, resulting in a base fire rate of 1.5 attacks per second.</p>
    </dd>

    <dt><a name="drought"></a><strong>Drought</strong> <img alt="Empty Potion Bottle" src="//i.imgur.com/Fwl3vlp.png" title="Empty Potion Bottle" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: Inflicted alongside Sick during the “survival” phases of <a href="/wiki/the-forgotten-king" title="The Forgotten King">The Forgotten King</a>, <a href="/wiki/black-blade-ozuchi" title="Black Blade Ozuchi">Black Blade Ozuchi</a> in the <a href="/wiki/hidden-interregnum" title="Hidden Interregnum">Hidden Interregnum</a>, and the bosses of the <a href="/wiki/moonlight-village" title="Moonlight Village">Moonlight Village</a>.</em> <br>
    Disables all consumable items and prevents them from being consumed for the duration of the status. This primarily includes <a href="/wiki/restoratives-and-boosters" title="Restoratives and Boosters">Restoratives and Boosters</a>, but also includes items such as <a href="/wiki/blueprints" title="Blueprints">Blueprints</a>, <a href="/wiki/dungeon-keys" title="Dungeon Keys">Dungeon Keys</a>, and so on.</p>
    </dd>

    <dt><a name="drunk"></a><strong>Drunk</strong> <img alt="Wine Bottle" src="//i.imgur.com/SDARewY.png" title="Wine Bottle" class="img-responsive"></dt>
    <dd>
    <p><em>Players: Self inflicted via the <a href="/wiki/ceremonial-merlot" title="Ceremonial Merlot">Ceremonial Merlot</a>, <a href="/wiki/pirate-rum" title="Pirate Rum">Pirate Rum</a>, <a href="/wiki/ghost-pirate-rum" title="Ghost Pirate Rum">Ghost Pirate Rum</a>, <a href="/wiki/saint-paddy-s-brew" title="Saint Paddy's Brew">Saint Paddy’s Brew</a>, <a href="/wiki/beach-party-madness-drinks" title="Beach Party Madness Drinks">Beach Party Madness Drinks</a>. <br>
    Enemies: used by <a href="/wiki/vintner-of-oryx" title="Vintner of Oryx">Vintners of Oryx</a> and <a href="/wiki/oryx-the-mad-god-3" title="Oryx the Mad God 3">Oryx the Mad God 3</a>.</em> <br>
    Blurs the screen if Hardware Acceleration is disabled, or heavily warps the screen if Hardware Acceleration is enabled. <br>
    If a player cannot see their gameplay while drunk, they may choose to turn off Hardware Acceleration to return Drunk to a blurry screen.</p>
    </dd>

    <dt><a name="exposed"></a><strong>Exposed</strong> <img alt="Grey Down Arrow" src="//i.imgur.com/rgu6wnZ.png" title="Grey Down Arrow" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by many of Samurais’ <a href="/wiki/wakizashi" title="Wakizashi">Wakizashi</a>, including Tiered starting from 3, the <a href="/wiki/crystal-key" title="Crystal Key">Crystal Key</a>, <a href="/wiki/oryxmas-ornament-exposed" title="Oryxmas Ornament: Exposed">Oryxmas Ornament: Exposed</a>, <a href="/wiki/ornaments-of-unity" title="Ornaments of Unity">Ornaments of Unity</a>. <br>
    Enemies: used by <a href="/wiki/killer-bee-queen" title="Killer Bee Queen">Killer Bee Queen</a>, <a href="/wiki/the-beekeeper" title="The Beekeeper">The Beekeeper</a>, <a href="/wiki/crystallised-crawler" title="Crystallised Crawler">Crystallised Crawlers</a> and <a href="/wiki/crystallised-boomer" title="Crystallised Boomer">Crystallised Boomers</a>.</em> <br>
    Reduces affected entity’s DEF by 20 during damage calculations. Affected targets <em>can</em> have their Defense reduced below 0, resulting in them taking more damage per shot. Exposed <em>does</em> affect Armor Piercing attacks and attacks on an Armor Broken target, making them deal 20 more damage per hit. As it affects defense calculations, Exposed is calculated before Cursed.</p>
    </dd>

    <dt><a name="hallucinating"></a><strong>Hallucinating</strong> <img alt="Mushroom" src="//i.imgur.com/UL2FD26.png" title="Mushroom" class="img-responsive"></dt>
    <dd>
    <p><em>Used by <a href="/wiki/magic-mushroom" title="Magic Mushroom">Magic Mushrooms</a>, <a href="/wiki/fairy-dust" title="Fairy Dust">Fairy Dust</a>, <a href="/wiki/forbidden-jungle" title="Forbidden Jungle">Masked Shamans</a>, <a href="/wiki/wishing-troll" title="Wishing Troll">Wishing Trolls</a>, <a href="/wiki/desire-troll" title="Desire Troll">Desire Troll</a> and the <a href="/wiki/seal-of-the-enchanted-forest" title="Seal of the Enchanted Forest">Seal of the Enchanted Forest</a>.</em> <br>
    Replaces objects and enemies on screen with random object or enemy sprites. Note that this does not actually change the object or enemy, but simply alters their appearance.</p>
    </dd>

    <dt><a name="hexed"></a><strong>Hexed</strong> <img alt="Mushroom" src="//i.imgur.com/UL2FD26.png" title="Mushroom" class="img-responsive"></dt>
    <dd>
    <p><em>Used by green pools in <a href="/wiki/mad-lab" title="Mad Lab">Mad Lab</a>, <a href="/wiki/transformation-potion" title="Transformation Potion">Transformation Potions</a>, <a href="/wiki/grotesque-scepter" title="Grotesque Scepter">Grotesque Scepter</a>, <a href="/wiki/wishing-troll" title="Wishing Troll">Wishing Trolls</a> and <a href="/wiki/desire-troll" title="Desire Troll">Desire Troll</a>.</em> <br>
    Replaces the player’s sprite with a random pet sprite.</p>
    </dd>

    <dt><a name="in-combat"></a><strong>In Combat</strong> (Icon - None)</dt>
    <dd>
    <p><em>Enemies: Used by the bosses of the <a href="/wiki/moonlight-village" title="Moonlight Village">Moonlight Village</a>.</em> <br>
    Forcibly puts the player in the “In Combat” state for a certain duration, regardless of whether or not the damage taken exceeded the player’s Combat Trigger. The duration of the debuff takes priority over the player’s normal IC timer.  <br>
    For more details on the status itself, see <a href="/wiki/vital-combat" title="Vital Combat">Vital Combat</a>.</p>
    </dd>

    <dt><a name="no effect"></a><strong>No Effect (Icon - None)</strong></dt>
    <dd>
    <p><em>Used by a players <a href="/wiki/pets" title="Pets">Pet</a> when another Status Effect blocks the useage of their <a href="/wiki/pet-abilities#heal" title="Pet Abilities">HP/MP Heal</a> ability, signified by red “No Effect” text appearing over the player when the ability is casted.</em> <br>
    The intended support is prevented by another Status Effect, changing the intended support  to instead remind No Effect.</p>
    </dd>

    <dt><a name="paralyzed"></a><strong>Paralyzed</strong> <img alt="Paralyze icon" src="//i.imgur.com/uXEglM6.png" title="Paralyze icon" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/blue-drake-egg" title="Blue Drake Egg">Blue Drake</a>, <a href="/wiki/quivers" title="Quivers">Archer’s Tiered Quivers</a>, <a href="/wiki/midnight-star" title="Midnight Star">Midnight Star</a>, <a href="/wiki/alien-core-power" title="Alien Core: Power">Alien Core: Power</a> and the <a href="/wiki/entropy-reactor" title="Entropy Reactor">Entropy Reactor</a>, and <a href="/wiki/orb-of-aether" title="Orb of Aether">Orb of Aether</a>. <br>
    Enemies: used by <a href="/wiki/tomb-thunder-turret" title="Tomb Thunder Turret">Tomb Thunder Turrets</a>, <a href="/wiki/lion-archer" title="Lion Archer">Lion Archers</a>, <a href="/wiki/ghost-of-skuld" title="Ghost of Skuld">Ghost of Skuld</a>, <a href="/wiki/scarab" title="Scarab">Scarabs</a>, <a href="/wiki/tomb-of-the-ancients#Nut" title="Tomb of the Ancients">Nut</a>, <a href="/wiki/coral-venom-trap" title="Coral Venom Trap">Coral Venom Trap</a>, <a href="/wiki/archer-puppet" title="Archer Puppet">Archer Puppets</a>, <a href="/wiki/cursed-grave" title="Cursed Grave">Cursed Grave</a>, <a href="/wiki/stone-guardian-sword" title="Stone Guardian Sword">Stone Guardian Sword</a>, <a href="/wiki/son-of-arachna" title="Son of Arachna">Son of Arachna</a>, <a href="/wiki/woodland-paralyze-turret" title="Woodland Paralyze Turret">Woodland Paralyze Turrets</a>, <a href="/wiki/corrupted-bowman" title="Corrupted Bowman">Corrupted Bowmen</a>, <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>, <a href="/wiki/marble-colossus" title="Marble Colossus">Marble Colossus</a>, and <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>.</em> <br>
    Renders entity completely immobile.</p>
    </dd>

    <dt><a name="pet-stasis"></a><strong>Pet Stasis</strong> <img alt="Pet Stasis icon" src="//i.imgur.com/X8XXlAr.png" title="Pet Stasis icon" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by various <a href="/wiki/lair-of-draconis" title="Lair of Draconis">Lair of Draconis</a> bosses, <a href="/wiki/the-puppet-master-encore" title="The Puppet Master (Encore)">The Puppet Master (Encore)</a>, all enemies found in <a href="/wiki/the-void" title="The Void">The Void</a>, Blue <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a>, various enemies in <a href="/wiki/oryx-s-sanctuary" title="Oryx's Sanctuary">Oryx’s Sanctuary</a>, <a href="/wiki/mystic-puppet" title="Mystic Puppet">Mystic Puppets</a>, <a href="/wiki/nightmare-colony" title="Nightmare Colony">Nightmare Colony</a>, <a href="/wiki/corrupted-sprite-and-corrupted-spirit" title="Corrupted Sprite and Corrupted Spirit">Corrupted Sprite and Corrupted Spirit</a>, <a href="/wiki/jade-and-garnet-statues" title="Jade and Garnet Statues">Jade and Garnet Statues</a>, <a href="/wiki/corrupted-spawn" title="Corrupted Spawn">Corrupted Spawn</a>, <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/spectral-sentry-event" title="Spectral Sentry (Event)">Spectral Sentry (Event)</a> and <a href="/wiki/spectral-sentry-lost-halls" title="Spectral Sentry (Lost Halls)">Spectral Sentry (Lost Halls)</a>.</em> <br>
    Turns player’s pet into a chicken, rendering it immobile and unable to use its abilities. Players who do not have a pet equipped cannot be inflicted with Pet Stasis.</p>
    </dd>

    <dt><a name="petrify"></a><strong>Petrify</strong> (Icon - None)</dt>
    <dd>
    <p><em>Players: Self inflicted via the <a href="/wiki/karma-orb" title="Karma Orb">Karma Orb</a>. <br>
    Enemies: used by <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/evil-spirit" title="Evil Spirit">Evil Spirits</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>, <a href="/wiki/golem-of-fear" title="Golem of Fear">Golem of Fear</a>, <a href="/wiki/marble-colossus" title="Marble Colossus">Marble Colossus</a> and <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>.</em> <br>
    Players are rendered unable to move or use weapons, but take 10% less damage from all attacks. Most abilities are unaffected by Petrify, and can still be used.</p>
    </dd>

    <dt><a name="quiet"></a><strong>Quiet</strong> <img alt="Word Bubble" src="//i.imgur.com/daPLggB.png" title="Word Bubble" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by <a href="/wiki/lair-vampire-king" title="Lair Vampire King">Lair Vampire Kings</a>, <a href="/wiki/fire-mage" title="Fire Mage">Fire Mages</a>, <a href="/wiki/fire-adept" title="Fire Adept">Fire Adepts</a>, <a href="/wiki/mysterious-crystal" title="Mysterious Crystal">Mysterious Crystal</a>, <a href="/wiki/oryx-the-mad-god" title="Oryx the Mad God">Oryx’s Simulacrum</a>, <a href="/wiki/oryx-the-mad-god-2" title="Oryx the Mad God 2">Oryx the Mad God</a>, <a href="/wiki/iceion" title="Iceion">Iceions</a>, <a href="/wiki/esben-the-unwilling" title="Esben the Unwilling">Esben the Unwilling</a>, <a href="/wiki/nut" title="Nut">Nut</a>, <a href="/wiki/sewer-brown-slime" title="Sewer Brown Slime">Sewer Brown Slime</a>, <a href="/wiki/crawling-spider-hatchling" title="Crawling Spider Hatchling">Crawling Spider Hatchlings</a>, <a href="/wiki/son-of-arachna" title="Son of Arachna">Son of Arachna</a>, <a href="/wiki/mammoth-megamoth" title="Mammoth Megamoth">Mammoth Megamoth</a>, <a href="/wiki/murderous-megamoth" title="Murderous Megamoth">Murderous Megamoth</a>, <a href="/wiki/pulsating-obstacle" title="Pulsating Obstacle">Pulsating Obstacle</a>, <a href="/wiki/swarm-colony" title="Swarm Colony">Swarm Colony</a>, <a href="/wiki/nightmare-colony" title="Nightmare Colony">Nightmare Colony</a>, <a href="/wiki/corrupted-armor" title="Corrupted Armor">Corrupted Armor</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a> and <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>.</em> <br>
    Completely drains MP, stops natural MP regeneration by WIS, and causes all forms of MP recovery to stop functioning. Fleeing to Nexus or entering a portal while Quieted will commonly restore the amount of MP to the player’s maximum base MP, even if they had little MP before getting quieted.</p>
    </dd>

    <dt><a name="sick"></a><strong>Sick</strong> <img alt="Skull" src="//i.imgur.com/vX0Ozp0.png" title="Skull" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by <a href="/wiki/bile-of-oryx" title="Bile of Oryx">Bile of Oryx</a>, <a href="/wiki/parasitic-blob" title="Parasitic Blob">Parasitic Blobs</a>, <a href="/wiki/parasitic-blob-scout" title="Parasitic Blob Scout">Parasitic Blob Scouts</a>, <a href="/wiki/parasitic-blob-guardian" title="Parasitic Blob Guardian">Parasitic Blob Guardians</a>, various <a href="/wiki/lair-of-draconis" title="Lair of Draconis">Lair of Draconis</a> bosses, <a href="/wiki/toxic-sewers" title="Toxic Sewers">Toxic Sewer</a> water, <a href="/wiki/kage-kami" title="Kage Kami">Kage Kami</a> and <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>.</em> <br>
    Stops natural HP regeneration by VIT, and causes all forms of HP recovery to stop functioning.</p>
    </dd>

    <dt><a name="silenced"></a><strong>Silenced</strong> <img alt="Crossed word bubble" src="//i.imgur.com/Y667IM7.png" title="Crossed word bubble" class="img-responsive"></dt>
    <dd>
    <p><em>Players: Self inflicted via the <a href="/wiki/dusky-catalyst" title="Dusky Catalyst">Dusky Catalyst</a>. Applied for 3 seconds when teleporting to another player or when entering the Realm (2 seconds if in a dungeon), along with <a href="#invincible">Invincible</a> and <a href="#stunned">Stunned</a>. Teleportation via <a href="/wiki/prisms" title="Prisms">Prisms</a>/<a href="/wiki/cloak-of-the-planewalker" title="Cloak of the Planewalker">Cloak of the Planewalker</a> does not apply silenced. <br>
    Enemies: used by <a href="/wiki/flayer-god" title="Flayer God">Flayer Gods</a>, <a href="/wiki/sprite-god" title="Sprite God">Sprite Gods</a>, <a href="/wiki/book-bomb" title="Book Bomb">Book Bombs</a>, <a href="/wiki/marble-defender" title="Marble Defender">Marble Defender</a>, <a href="/wiki/archbishop-leucoryx" title="Archbishop Leucoryx">Archbishop Leucoryx</a>, <a href="/wiki/chancellor-dammah" title="Chancellor Dammah">Chancellor Dammah</a>, <a href="/wiki/marble-colossus" title="Marble Colossus">Marble Colossus</a> and <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>.</em> <br>
    Prevents player from using their ability. Unlike Quiet, Silenced does not deplete the player’s MP or stop MP recovery.</p>
    </dd>

    <dt><a name="slowed"></a><strong>Slowed</strong> <img alt="Red Down Arrow" src="//i.imgur.com/SBXUz7e.png" title="Red Down Arrow" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/green-drake-egg" title="Green Drake Egg">Green Drake</a>, <a href="/wiki/freezing-quiver" title="Freezing Quiver">Freezing Quiver</a> and all three <a href="/wiki/beehemoth-quiver" title="Beehemoth Quiver">Beehemoth Quivers</a>, <a href="/wiki/traps" title="Traps">Huntress’s Traps</a>, <a href="/wiki/scepter-of-fulmination" title="Scepter of Fulmination">Scepter of Fulmination</a>, <a href="/wiki/orb-of-aether" title="Orb of Aether">Orb of Aether</a>, <a href="/wiki/orb-of-sweet-demise" title="Orb of Sweet Demise">Orb of Sweet Demise</a>, <a href="/wiki/shield-of-flowing-clarity" title="Shield of Flowing Clarity">Shield of Flowing Clarity</a>, <a href="/wiki/ronin-s-wakizashi" title="Ronin's Wakizashi">Ronin’s Wakizashi</a>, <a href="/wiki/chief-s-war-horn" title="Chief's War Horn">Chief’s War Horn</a>. Self inflicted via <a href="/wiki/cloak-of-bloody-surprises" title="Cloak of Bloody Surprises">Cloak of Bloody Surprises</a>, <a href="/wiki/challenger-helm" title="Challenger Helm">Challenger Helm</a>, and <a href="/wiki/star-of-enlightenment" title="Star of Enlightenment">Star of Enlightenment</a>. <br>
    Enemies: used by <a href="/wiki/arachna-element" title="Arachna Element">Arachna’s Web</a>, <a href="/wiki/stheno-pet" title="Stheno Pet">Stheno’s Pets</a>, <a href="/wiki/lair-vampire" title="Lair Vampire">Lair Vampires</a>, <a href="/wiki/encore-trap" title="Encore Trap">Encore Traps</a>, <a href="/wiki/slime-god" title="Slime God">Slime Gods</a>, <a href="/wiki/gulpord-the-slime-god" title="Gulpord the Slime God">Gulpord the Slime God</a>, <a href="/wiki/oryx-the-mad-god" title="Oryx the Mad God">Oryx’s Simulacrum</a>, <a href="/wiki/oryx-the-mad-god-2" title="Oryx the Mad God 2">Oryx the Mad God</a>, <a href="/wiki/bile-of-oryx" title="Bile of Oryx">Bile of Oryx</a>, <a href="/wiki/sewer-yellow-slime" title="Sewer Yellow Slime">Sewer Yellow Slimes</a>, <a href="/wiki/goblin-warlock" title="Goblin Warlock">Goblin Warlocks</a>, <a href="/wiki/guardian-of-the-lost-lands" title="Guardian of the Lost Lands">Guardians of the Lost Lands</a>, <a href="/wiki/small-creampuff" title="Small Creampuff">Small Creampuffs</a>, <a href="/wiki/deadwater-docks-parrot" title="Deadwater Docks Parrot">Deadwater Docks Parrots</a>, <a href="/wiki/deadwater-docks-macaw" title="Deadwater Docks Macaw">Deadwater Docks Macaws</a>, <a href="/wiki/painling" title="Painling">Painlings</a>, <a href="/wiki/pterasite-bomb" title="Pterasite Bomb">Pterasite Bombs</a>, <a href="/wiki/jade-and-garnet-statues" title="Jade and Garnet Statues">Jade and Garnet Statues</a>, <a href="/wiki/corrupted-monk" title="Corrupted Monk">Corrupted Monks</a>, <a href="/wiki/corrupted-spearman" title="Corrupted Spearman">Corrupted Spearmen</a>, <a href="/wiki/stone-ranger" title="Stone Ranger">Stone Rangers</a>, <a href="/wiki/daichi-the-fallen" title="Daichi the Fallen">Daichi the Fallen</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>, <a href="/wiki/spectral-sentry-event" title="Spectral Sentry (Event)">Spectral Sentry (Event)</a>, <a href="/wiki/spectral-sentry-lost-halls" title="Spectral Sentry (Lost Halls)">Spectral Sentry (Lost Halls)</a>, Green <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a> and Snowflakes.</em> <br>
    Effect on enemy: Reduces enemy movement speed by 50%. <br>
    Effect on player: Reduces player SPD to 0 during movement speed calculation, resulting in a base speed of 4 tiles/second. Nullifies effects of Speedy.</p>
    </dd>

    <dt><a name="stasis"></a><strong>Stasis</strong> (Icon - None)</dt>
    <dd>
    <p><em>Players: used by many of Mystic’s <a href="/wiki/orbs" title="Orbs">Orbs</a>, <a href="/wiki/gravel" title="Gravel">Gravel</a>, <a href="/wiki/orange-drake-egg" title="Orange Drake Egg">Orange Drake</a> and <a href="/wiki/lightning-in-a-bottle" title="Lightning in a Bottle">Lightning in a Bottle</a>.</em> <br>
    Affected enemy turns gray and cannot move or attack, but also cannot be hit or damaged. All enemies put into Stasis get three seconds of Stasis Immunity after it wears off.</p>
    </dd>
    </dl>

    <p><a name="stat-reduction"></a><strong>Stat Reduction <img alt="HP↓" src="//i.imgur.com/X8PSA8E.png" title="HP↓" class="img-responsive"><img alt="MP↓" src="//i.imgur.com/blYMDGs.png" title="MP↓" class="img-responsive"><img alt="ATT↓" src="//i.imgur.com/N8WaZbg.png" title="ATT↓" class="img-responsive"><img alt="DEF↓" src="//i.imgur.com/QVLrXSV.png" title="DEF↓" class="img-responsive"><img alt="SPD↓" src="//i.imgur.com/L6M6Ixd.png" title="SPD↓" class="img-responsive"><img alt="DEX↓" src="//i.imgur.com/DL5i7nn.png" title="DEX↓" class="img-responsive"><img alt="VIT↓" src="//i.imgur.com/wpxNMNc.png" title="VIT↓" class="img-responsive"><img alt="WIS↓" src="//i.imgur.com/GVwmKke.png" title="WIS↓" class="img-responsive"></strong> <br>
    <em>Players: Self inflicted via <a href="/wiki/valor" title="Valor">Valor</a>, <a href="/wiki/warmonger" title="Warmonger">Warmonger</a>, the <a href="/wiki/resurrected-warrior-s-armor" title="Resurrected Warrior's Armor">Resurrected Warrior’s Armor</a>, <a href="/wiki/crystal-shield" title="Crystal Shield">Crystal Shield</a>, <a href="/wiki/helm-of-exalted-might" title="Helm of Exalted Might">Helm of Exalted Might</a>, <a href="/wiki/seal-of-the-enchanted-forest" title="Seal of the Enchanted Forest">Seal of the Enchanted Forest</a>, <a href="/wiki/ceremonial-merlot" title="Ceremonial Merlot">Ceremonial Merlot</a>, <a href="/wiki/resplendent-bow" title="Resplendent Bow">Resplendent Bow</a>, <a href="/wiki/tincture-of-courage" title="Tincture of Courage">Tincture of Courage</a>, and <a href="/wiki/tincture-of-fear" title="Tincture of Fear">Tincture of Fear</a>.</em> <br>
    Player’s stats are temporarily decreased. The amount of the reduction depends on the source of the debuff. If multiple reductions from one source are stacked, every successive reduction will only be half as strong as the previous one. If multiple reductions from different sources are acquired (eg. two SPD reductions from a <a href="/wiki/crystal-shield" title="Crystal Shield">Crystal Shield</a> and a <a href="/wiki/tincture-of-courage" title="Tincture of Courage">Tincture of Courage</a>), the strongest one will override the others. </p>

    <dl>
    <dt><a name="stunned"></a><strong>Stunned</strong> <img alt="Gold Five Pointed Star" src="//i.imgur.com/Yg7B9DK.png" title="Gold Five Pointed Star" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by many <a href="/wiki/shields" title="Shields">Shields</a>, <a href="/wiki/grotesque-scepter" title="Grotesque Scepter">Grotesque Scepter</a>, and <a href="/wiki/ballistic-star" title="Ballistic Star">Ballistic Star</a>. Applied for 3 seconds when teleporting to another player or when entering a new area (2 seconds while teleporting inside dungeons), along with <a href="#invincible">Invincible</a> and <a href="#silenced">Silenced</a>. Teleportation via <a href="/wiki/prisms" title="Prisms">Prisms</a>/<a href="/wiki/cloak-of-the-planewalker" title="Cloak of the Planewalker">Cloak of the Planewalker</a> does not apply stunned. <br>
    Enemies: <a href="/wiki/sarcophagus" title="Sarcophagus">Sarcophagus</a>, <a href="/wiki/bes" title="Bes">Bes</a>, <a href="/wiki/stone-knight" title="Stone Knight">Stone Knights</a>, <a href="/wiki/ghost-ship-rat" title="Ghost Ship Rat">Ghost Ship Rats</a>, <a href="/wiki/bookwyrm" title="Bookwyrm">Bookwyrms</a>, <a href="/wiki/desire-troll" title="Desire Troll">Desire Troll</a>, <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>, <a href="/wiki/oryx-the-mad-god-3" title="Oryx the Mad God 3">Oryx the Mad God 3</a>, and green pools from the <a href="/wiki/mad-lab" title="Mad Lab">Mad Lab</a>.</em> <br>
    Effect on enemy: Enemy is unable to fire bullets; certain attacks like bombs, AoEs, and minion summoning may be exempt. <br>
    Effect on player: Player cannot use their weapon, but can still use abilities.</p>
    </dd>

    <dt><a name="unstable"></a><strong>Unstable</strong> <img alt="Unstable Arrow" src="//i.imgur.com/XmbR7bc.png" title="Unstable Arrow" class="img-responsive"></dt>
    <dd>
    <p><em>Enemies: used by <a href="/wiki/avatar-of-the-forgotten-king" title="Avatar of the Forgotten King">Avatar of the Forgotten King</a>, some enemies in <a href="/wiki/the-shatters" title="The Shatters">The Shatters</a>, <a href="/wiki/jade-and-garnet-statues" title="Jade and Garnet Statues">Jade Statue</a>, <a href="/wiki/soulblast" title="Soulblast">Soulblasts</a>, <a href="/wiki/snow-bat-mama" title="Snow Bat Mama">Snow Bat Mamas</a>, <a href="/wiki/esben-the-unwilling" title="Esben the Unwilling">Esben the Unwilling</a>, <a href="/wiki/oryx-cleric" title="Oryx Cleric">Oryx Clerics</a>, <a href="/wiki/lost-sentry" title="Lost Sentry">Lost Sentry</a>, <a href="/wiki/void-entity" title="Void Entity">Void Entity</a>, <a href="/wiki/sewer-rat" title="Sewer Rat">Sewer Rats</a> and <a href="/wiki/server-heart" title="Server Heart">Server Heart</a>.</em> <br>
    Weapons gain random shot deviation when aiming (limited to a certain angle), significantly lowering accuracy. Abilities that require aiming (spells, poisons, etc) will fire in random directions.</p>
    </dd>

    <dt><a name="weak"></a><strong>Weak</strong> <img alt="Weak icon" src="//i.imgur.com/cX1cbMB.png" title="Weak icon" class="img-responsive"></dt>
    <dd>
    <p><em>Players: used by <a href="/wiki/scepter-of-rust" title="Scepter of Rust">Scepter of Rust</a>, <a href="/wiki/pharaoh-s-requiem" title="Pharaoh's Requiem">Pharaoh’s Requiem</a>, <a href="/wiki/oryxmas-ornament-weak" title="Oryxmas Ornament: Weak">Oryxmas Ornament: Weak</a>, and <a href="/wiki/ornaments-of-unity" title="Ornaments of Unity">Ornaments of Unity</a>. <br>
    Enemies: used by various bosses, <a href="/wiki/earth-golem" title="Earth Golem">Earth Golems</a>, <a href="/wiki/urgle" title="Urgle">Urgles</a>, White <a href="/wiki/marble-colossus-pillar" title="Marble Colossus Pillar">Marble Colossus Pillars</a>/<a href="/wiki/marble-colossus-rock" title="Marble Colossus Rock">Rocks</a>, <a href="/wiki/crystal-prisoner-steed" title="Crystal Prisoner Steed">Crystal Prisoner Steeds</a>, and <a href="/wiki/server-heart" title="Server Heart">Server Heart</a>.</em> <br>
    Effect on enemy: Reduces damage of all attacks by 10%. <br>
    Effect on player: Reduces player ATT to 0 during damage calculations (Base, 50% weapon damage).</p>
    </dd>
    </dl>
    </div>
    """
    status_effects = parse_status_effects(sample_html)
def test_parse_player_data_1():
    """Test case for user KatsFan."""
    sample_html = """
    <html>
        <h1>
            <span class="entity-name">KatsFan</span>
        </h1>
        <div class="row">
            <div class="col-md-5">
                <table class="summary">
                <tr>
                    <td>Characters</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td>Skins</td>
                    <td>
                    <span class="numeric">40</span> (32494 <sup>th</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Exaltations</td>
                    <td>
                    <span class="numeric">8</span>
                    </td>
                </tr>
                <tr>
                    <td>Fame</td>
                    <td>
                    <span class="numeric">16108</span> (7492 <sup>nd</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Rank</td>
                    <td>
                    <div class="star-container">51 <div class="star star-red"></div>
                    </div>
                    </td>
                </tr>
                <tr>
                    <td>Account fame</td>
                    <td>
                    <span class="numeric">108005</span> (4348 <sup>th</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Guild</td>
                    <td>
                    <a href="/guild/TowerJanitors">TowerJanitors</a>
                    </td>
                </tr>
                <tr>
                    <td>Guild Rank</td>
                    <td>Initiate</td>
                </tr>
                <tr>
                    <td>First seen</td>
                    <td>~6 years and 289 days ago</td>
                </tr>
                <tr>
                    <td>Last seen</td>
                    <td>
                    <span class="timeago" title="2024-01-18T15:15:09Z">2024-01-18 15:15:09</span> as Priest
                    </td>
                </tr>
                </table>
            </div>
            <div class="col-md-7">
                <div class="well description" id="d">
                <div class="line1 description-line">Hello!</div>
                <div class="line2 description-line">I play on Steam</div>
                <div class="line3 description-line">I took a break, came back and urgles are still annoying</div>
                </div>
            </div>
        </div>
    </html>
    """

    player = parse_player_data(sample_html)

    assert player.name == "KatsFan"
    assert player.characters_count == 8
    assert player.description == ['Hello!', 'I play on Steam', 'I took a break, came back and urgles are still annoying']
    assert player.characters_count == 8
    assert player.skins == 40
    assert player.exaltations == 8
    assert player.fame == 16108
    assert player.rank == 51
    assert player.account_fame == 108005
    assert player.guild == 'TowerJanitors'
    assert player.guild_rank == 'Initiate'
    assert player.first_seen == '~6 years and 289 days ago'
    assert player.created is None
    assert player.last_seen == '2024-01-18 15:15:09 as Priest'
    assert player.characters is None

def test_parse_player_data_2():
    """Test case for user Lollynick."""
    sample_html = """
    <html>
        <h1>
            <span class="entity-name">Lollynick</span>
        </h1>
        <div class="row">
            <div class="col-md-5">
            <table class="summary">
                <tr>
                <td>Characters</td>
                <td>5</td>
                </tr>
                <tr>
                <td>Skins</td>
                <td>
                    <span class="numeric">60</span> (17018 <sup>th</sup>)
                </td>
                </tr>
                <tr>
                <td>Exaltations</td>
                <td>
                    <span class="numeric">79</span>
                </td>
                </tr>
                <tr>
                <td>Fame</td>
                <td>
                    <span class="numeric">1787</span> (19790 <sup>th</sup>)
                </td>
                </tr>
                <tr>
                <td>Rank</td>
                <td>
                    <div class="star-container">56 <div class="star star-orange"></div>
                    </div>
                </td>
                </tr>
                <tr>
                <td>Account fame</td>
                <td>
                    <span class="numeric">616994</span> ( <a href="/top-players-by-account-fame/301">396 <sup>th</sup>
                    </a>)
                </td>
                </tr>
                <tr>
                <td>Guild</td>
                <td>
                    <a href="/guild/TowerJanitors">TowerJanitors</a>
                </td>
                </tr>
                <tr>
                <td>Guild Rank</td>
                <td>Leader</td>
                </tr>
                <tr>
                <td>Created</td>
                <td>~11 years and 34 days ago</td>
                </tr>
                <tr>
                <td>Last seen</td>
                <td>hidden</td>
                </tr>
            </table>
            </div>
            <div class="col-md-7">
            <div class="well description" id="d">
                <div class="line1 description-line">gKYdTzvrUOTr8Kdh0Be0</div>
                <div class="line2 description-line"></div>
                <div class="line3 description-line"></div>
            </div>
            </div>
        </div>
    </html>
    """

    player = parse_player_data(sample_html)

    assert player.name == "Lollynick"
    assert player.characters_count == 5
    assert player.description == ['gKYdTzvrUOTr8Kdh0Be0', '', '']
    assert player.skins == 60
    assert player.exaltations == 79
    assert player.fame == 1787
    assert player.rank == 56
    assert player.account_fame == 616994
    assert player.guild == 'TowerJanitors'
    assert player.guild_rank == 'Leader'
    assert player.first_seen is None
    assert player.created == '~11 years and 34 days ago'
    assert player.last_seen == 'hidden'
    assert player.characters is None