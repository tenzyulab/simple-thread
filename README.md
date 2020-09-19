# Simple Thread

![eyecatch](https://cdn.discordapp.com/attachments/752286472383758416/756862024499200051/image0.jpg)

> Simple Thread is a Discord Bot that allows you to add threaded features to your guild.

### **[✉️ Invite to your server](https://discord.com/api/oauth2/authorize?client_id=754309543160184893&permissions=8&scope=bot)**

## How to add the Thread?

### `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`

Setup the Thread to your server by this command.

These will be in a pair. If you don't duplicate IDs, you can add as many Thread as you like.

Please specify these arguments by ID You can also use a name, but the ID is more reliable.

## How to remove the Thread?

### `/remove <ThreadMasterChannel>`

Remove a Thread containing the Thread Master Channel by this command.

Please specify these arguments by ID. You can also use the channel name, but the ID is more reliable.

## How to Use the Thread

### `Send a Thread Name to the Thread Master Channel`

Create a thread with the same name as the message sent in the Thread Category.

### `/rename <name>`

If your channel, rename to the `<name>`.

Note: Due to a limitation on the discord side, the same channel name is updated only twice every 10 minutes.

### `/close`

If your channel, move to the Archive Category.

Tips: Patrol? If you're <b>an administrator</b>, you can close it <b>indiscriminately</b>. Let's keep the server secure!

### `Sorted by Unread Order`

Threads below the Thread Master Channel are automatically sorted in unread order.

Don't mind about which channel is being updated, take a peek at it from above!

### `/help`

Shows the help.

## Required Permissions

- Administrator

### Why Requires Admin?

Sorry, this bot use the method `sync_permission()`; needed the admin to use.

We're looking for a solution to this problem of asking for too strong permissions.

### NOTE

1. I wrote some hackneyed code. I wanna the Code Reviews from you.
2. I'm not native English speakers, So I'm always open to better translations from you.
3. I've done some testing, but there are always unknown problems. I welcome your reports to the issue.

### Special Thanks

- HiraginoYuki https://github.com/HiraginoYuki
