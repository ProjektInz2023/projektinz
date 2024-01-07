provider "azurerm" {
  features = {}
}

resource "azurerm_resource_group" "kantyna-resource-group" {
  name     = "kantyna-resource-group"
  location = "Europe West"
}

resource "azurerm_sql_server" "example" {
  name                         = "example-sql-server"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = ".env.password"
}

resource "azurerm_sql_database" "example" {
  name                = "example-sql-db"
  resource_group_name = azurerm_resource_group.example.name
  server_name         = azurerm_sql_server.example.name
  edition             = "Standard"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_gb         = 1
}

resource "azurerm_synapse_workspace" "example" {
  name                = "example-synapse-workspace"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
}

resource "azurerm_synapse_sql_pool" "example" {
  name                = "example-synapse-sql-pool"
  resource_group_name = azurerm_resource_group.example.name
  workspace_name      = azurerm_synapse_workspace.example.name
  location            = azurerm_resource_group.example.location
  sku {
    name = "DW100c"
  }
}