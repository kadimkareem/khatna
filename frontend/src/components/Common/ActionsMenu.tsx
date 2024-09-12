import React from 'react'
import {
  Button,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  useDisclosure,
} from '@chakra-ui/react'
import { BsThreeDotsVertical } from 'react-icons/bs'
import { FiEdit, FiTrash } from 'react-icons/fi'

import EditUser from '../Admin/EditUser'
import EditItem from '../Items/EditItem'
import EditCar from '../Cars/EditCar'  // Import the EditCar component
import Delete from './DeleteAlert'
import { ItemOut, UserOut, CarOut } from '../../client'  // Add CarOut to imports

interface ActionsMenuProps {
  type: 'User' | 'Item' | 'Car'  // Add 'Car' as an option
  value: ItemOut | UserOut | CarOut  // Include CarOut in the value type
  disabled?: boolean
}

const ActionsMenu: React.FC<ActionsMenuProps> = ({ type, value, disabled }) => {
  const editUserModal = useDisclosure()
  const deleteModal = useDisclosure()

  return (
    <>
      <Menu>
        <MenuButton
          isDisabled={disabled}
          as={Button}
          rightIcon={<BsThreeDotsVertical />}
          variant="unstyled"
        ></MenuButton>
        <MenuList>
          <MenuItem
            onClick={editUserModal.onOpen}
            icon={<FiEdit fontSize="16px" />}
          >
            Edit {type}
          </MenuItem>
          <MenuItem
            onClick={deleteModal.onOpen}
            icon={<FiTrash fontSize="16px" />}
            color="ui.danger"
          >
            Delete {type}
          </MenuItem>
        </MenuList>
        {type === 'User' && (
          <EditUser
            user={value as UserOut}
            isOpen={editUserModal.isOpen}
            onClose={editUserModal.onClose}
          />
        )}
        {type === 'Item' && (
          <EditItem
            item={value as ItemOut}
            isOpen={editUserModal.isOpen}
            onClose={editUserModal.onClose}
          />
        )}
        {type === 'Car' && (
          <EditCar  // Render EditCar component when the type is 'Car'
            car={value as CarOut}
            isOpen={editUserModal.isOpen}
            onClose={editUserModal.onClose}
          />
        )}
        <Delete
          type={type}
          id={value.id}
          isOpen={deleteModal.isOpen}
          onClose={deleteModal.onClose}
        />
      </Menu>
    </>
  )
}

export default ActionsMenu