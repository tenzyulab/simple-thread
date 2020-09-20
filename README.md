# Simple Thread

![eyecatch](https://cdn.discordapp.com/attachments/752286472383758416/757135343030894612/image0.jpg)

> Simple Thread is a Discord Bot that allows you to implement thread features in a better way.

### **[✉️ Invite to your server](https://discord.com/api/oauth2/authorize?client_id=754309543160184893&permissions=8&scope=bot)**

## Usage

### `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`

Sets the Thread to your server.

If you don't duplicate IDs, you can add as many threads as you like.

Please pass these arguments by ID. You can also use a name, but the ID is more reliable.

### `/remove <ThreadMasterChannel>`

Removes the saved Thread features with the set command.

Channels and categories will not be deleted.

### `<ThreadName>`

When you send it to `<ThreadMasterChannel>`, Simple Thread creates a new channel named `<ThreadName>` in `<ThreadCategory>`.

Tips: If `<ArchiveCategory>` has a channel named `<ThreadName>`, it is reopened.

### `/reopen`

When you send it to closed channel in `<ArchiveCategory>`, it is reopened.

Tips: If your server is making the archive category unwritable, please refer to the Tips in `<ThreadName>`.

### `/rename <ThreadName>`

Renames the channel to `<ThreadName>` only if sent to your channel by you.

Note: Due to a limitation on the discord side, on the same channel, the channel name is only updated twice in 10 minutes.

### `/close`

Archives the channel to `<ArchiveCategory>` only if sent to your channel by you.

Tips: Patrol? If you're <b>an administrator</b>, you can close it <b>indiscriminately</b>. Let's keep the server secure!

### `/help`

Shows the help.

## Others

### `Sorted by Unread Order`

Each thread moves to the next position of the thread master when a new message comes in.

Don't care which channel is updated.

Just tap the thread from the top!

## Required Permissions

- Administrator

### Why Requires Admin?

Sorry, this bot uses the method `sync_permission()`; needed the admin to use.

We're looking for a solution to this problem of asking for too strong permissions.

## NOTE

1. I think I wrote some hackneyed code. I want you to code reviews.
2. I'm not native English speakers, So I'm always open to better translations from you.
3. I've done some testing, but there are always unknown problems. I welcome your reports to the issue.

## Special Thanks

### HiraginoYuki - https://github.com/hiraginoyuki

He is also Japanese, but he worked with me from the development stage to come up with English expression.
